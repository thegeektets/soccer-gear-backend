from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Product(models.Model):
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    title = models.CharField(null=False, blank=False, max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=1000, default=0)
    description = models.TextField(null=False, blank=False, max_length=255)
    size = JSONField(blank=True)
    color = JSONField(blank=True)
    main_image = models.CharField(null=False, blank=True, max_length=255)
    images = JSONField(blank=True)
    video = models.CharField(null=False, blank=True, max_length=255)
    category = models.ManyToManyField('products.Category')

    def __str__(self):
        return "%s" % (self.title)


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    title = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return "%s" % (self.title)


