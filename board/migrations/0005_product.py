# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-06 23:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0004_remove_board_text2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_image', models.TextField()),
                ('text', models.TextField()),
                ('view_hit', models.IntegerField()),
                ('purchased', models.IntegerField()),
                ('like', models.IntegerField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mod_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
