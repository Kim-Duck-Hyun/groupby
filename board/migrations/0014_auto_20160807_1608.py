# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-07 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20160807_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.TextField(default=2016),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.TextField(default=20160725),
            preserve_default=False,
        ),
    ]