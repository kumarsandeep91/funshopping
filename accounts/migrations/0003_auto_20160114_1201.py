# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_details_u_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='sex',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
