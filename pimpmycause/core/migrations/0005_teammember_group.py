# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-21 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_teammember_visual_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='group',
            field=models.IntegerField(choices=[(0, 'Core'), (1, 'Advisory Board'), (2, 'Ambassadors')], default=1),
        ),
    ]
