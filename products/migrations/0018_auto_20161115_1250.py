# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20161115_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='parent',
            new_name='product',
        ),
    ]
