# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160114_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='image',
            field=models.CharField(default='default.png', max_length=50),
        ),
    ]
