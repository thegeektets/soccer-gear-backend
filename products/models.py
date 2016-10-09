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
    description = models.TextField(null=False, blank=False)
    attributes = JSONField(blank=True, default={})
    attribute_fields = JSONField(blank=True, default=[])
    main_image = models.ImageField(null=True, blank=True, upload_to="product_images/")
    images = JSONField(blank=True)
    video = models.CharField(null=False, blank=True, max_length=255)
    category = models.ManyToManyField('products.Category')

    def __str__(self):
        return "%s" % (self.title)


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('title',)
    title = models.CharField(null=False, blank=False, max_length=255)
    parent = models.ForeignKey('products.Category', null=True, blank=True)

    def __str__(self):
        return "%s" % (self.title)


    def get_children(self):
        return Category.objects.filter(parent=self)
