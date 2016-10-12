# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20161009_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='products.Category'),
        ),
    ]