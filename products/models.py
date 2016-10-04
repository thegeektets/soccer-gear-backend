from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Product(models.Model):
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    title = models.CharField(null=False, blank=False, max_length=255)
    price = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank=False, max_length=255)
    size = JSONField()
    color = JSONField()
    main_image = models.CharField(null=False, blank=False, max_length=255)
    images = JSONField()
    video = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return "%s" % (self.title)


    # TODO: make this the correct field on the products model
class ProductCategory(models.Model):
    class Meta:
        verbose_name = _('ProductCategory')
        verbose_name_plural = _('Product_Categories')

    product = models.ForeignKey('products.Product', null=False, blank=False)
    category = models.ForeignKey('products.Category', null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.product, self.category)


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    title = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return "%s" % (self.title)


