# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-08 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18, max_length=6),
        ),
    ]
