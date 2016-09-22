# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0006_auto_20160921_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='middle_name'),
        ),
    ]
