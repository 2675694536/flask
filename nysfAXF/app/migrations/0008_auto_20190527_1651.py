# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-27 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_goods'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='goods',
            table='axf_goods',
        ),
    ]
