# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-24 08:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0005_changepassword'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChangePassword',
        ),
    ]