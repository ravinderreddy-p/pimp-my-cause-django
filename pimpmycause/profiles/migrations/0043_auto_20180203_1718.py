# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-03 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0042_auto_20180203_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pimpuser',
            name='linkedin',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='pimpuser',
            name='twitter',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='pimpuser',
            name='website',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
