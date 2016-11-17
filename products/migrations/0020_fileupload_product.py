# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_fileupload_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]