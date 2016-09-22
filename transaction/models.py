from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
import django.utils.timezone
from product.models import Product
# Create your models here.


class Order(models.Model):

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    user = models.ForeignKey('custom_auth.User', null=False, blank=False)
    status = models.CharField(null=False, blank=False, max_length=255)
    payment = models.ForeignKey('transaction.Payment', null=True, blank=False)
    cost = models.CharField(null=False, blank=False, max_length=255)
    date_ordered = models.DateField(default= django.utils.timezone.now, null=False, blank=False, max_length=255)

    def __str__(self):
        return "%s - %s %s %s %s" % (self.user, self.status, self.payment, self.cost, self.date_ordered)

class Order_Item(models.Model):
    class Meta:
        verbose_name = _('Order_Item')
        verbose_name_plural = _('Order_Items')

    user = models.ForeignKey('custom_auth.User', null=False, blank=False)
    order = models.ForeignKey('transaction.Order', null=False, blank=False)
    product = models.ForeignKey('product.Product', null=False, blank=False)
    price = models.CharField(null=False, blank=False, max_length=255)
    quantity = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return "%s - %s %s %s %s" % (self.user, self.order, self.product, self.price, self.quantity)


class Payment(models.Model):
    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    user = models.ForeignKey('custom_auth.User', null=False, blank=False)
    mpesa_code = models.CharField(null=False, blank=False, max_length=255)
    date_paid = models.DateField(default= django.utils.timezone.now, null=False, blank=False, max_length=255)

    def __str__(self):
        return "%s %s %s" %(self.user, self.mpesa_code, self.date_paid)
