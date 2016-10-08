from decimal import Decimal

from django.contrib.postgres.fields.jsonb import JSONField
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.manager import Manager
from django.utils.translation import ugettext_lazy as _
from products.models import Product


class CartManager(Manager):

    def get_for_user_or_session(self, user, session_key):
        to_return = None
        if session_key is not None:
            try:
                # need to upgrade the cart to a user cart in this situation
                session_cart = self.get(session=session_key)
            except ObjectDoesNotExist as e:
                session_cart = None

        if user.is_anonymous() is True:
            return session_cart
        else:
            try:
                cart_for_user = self.get(user=user)
            except ObjectDoesNotExist as e:
                cart_for_user = None

            if session_cart is not None and cart_for_user is not None:
                for item in session_cart.items.all():
                    item.cart = cart_for_user
                    cart_for_user.items.add(item)
                    cart_for_user.total_quantity += item.quantity
                cart_for_user.subtotal_cart()
                cart_for_user.save()
                session_cart.delete()
                return cart_for_user
            elif session_cart is None and cart_for_user is not None:
                return cart_for_user
            if session_cart is not None and cart_for_user is None:
                # need to upgrade the cart to a user cart in this situation
                session_cart = self.get(session=session_key)
                session_cart.user = user
                session_cart.session = None
                session_cart.save()
                return session_cart

        return to_return

    def get_or_create_for_user_or_session(self, user, session_key):
        to_return = None
        try:
            if user.is_anonymous() and session_key is not None:
                to_return = self.get(session=session_key)
            if user.is_anonymous() is False:
                to_return = self.get(user=user)
        except ObjectDoesNotExist as e:
            to_return = None

        if to_return is None:
            if user.is_anonymous() and session_key is not None:
                to_return = self.create(session=session_key)
            if user.is_anonymous() is False:
                to_return = self.create(user=user)

        return to_return


class Cart(models.Model):

    objects = CartManager()

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    total_quantity = models.IntegerField(null=False, blank=False, default=0)
    # if a user in authenticated then this links the cart to the user
    user = models.ForeignKey('custom_auth.User', null=True, blank=True)
    # if a user in anonymous this links the cart to the user
    session = models.CharField(null=True, blank=True, max_length=255)
    subtotal = models.DecimalField(decimal_places=2, max_digits=1000, default=0)

    def __str__(self):
        return "Cart - %s" % (
            self.total_quantity
        )

    def add_item(self, product_id, chosen_attributes):
        product = Product.objects.get(id=product_id)
        try:
            check = self.items.get(product_id=product_id, chosen_attributes=chosen_attributes)
            check.quantity += 1
            check.save()
        except ObjectDoesNotExist as e:
            self.items.add(CartItem.objects.create(
                cart=self,
                product=product,
                chosen_attributes=chosen_attributes
            ))
        self.total_quantity += 1
        self.subtotal_cart()
        self.save()
        return self

    def remove_item(self, cart_item_id):
        try:
            cart_item = self.items.get(id=cart_item_id)
            self.total_quantity = self.total_quantity - cart_item.quantity
            cart_item.delete()
            self.subtotal_cart()
            self.save()
            return self
        except ObjectDoesNotExist as e:
            return self

    def update_quantity_for_item(self, cart_item_id, quantity):
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            self.total_quantity -= cart_item.quantity
            cart_item.quantity = quantity
            self.total_quantity += cart_item.quantity
            cart_item.save()
            self.subtotal_cart()
            self.save()
            return self
        except ObjectDoesNotExist as e:
            return self

    def subtotal_cart(self):
        subtotal = 0;
        for item in self.items.all():
            subtotal += item.product.price * item.quantity

        self.subtotal = subtotal

class CartItem(models.Model):
    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

    cart = models.ForeignKey('cart.Cart', null=False, blank=False, related_name='items')
    product = models.ForeignKey('products.Product', null=False, blank=False)
    chosen_attributes = JSONField(default={})
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Cart Item - %s" % (
            self.product
        )