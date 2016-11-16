# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20161115_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datafile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.FileUpload'),
            preserve_default=False,
        ),
    ]
