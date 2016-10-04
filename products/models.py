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


