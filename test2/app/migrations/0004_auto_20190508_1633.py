# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-08 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190508_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
