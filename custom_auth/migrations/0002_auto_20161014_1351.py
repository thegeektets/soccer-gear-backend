# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-14 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mpesa_id',
        ),
        migrations.AddField(
            model_name='user',
            name='mpesa_phone_number',
            field=models.TextField(blank=True, max_length=30, verbose_name='mpesa_phone_number'),
        ),
    ]
