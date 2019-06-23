# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-27 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=126)),
                ('name', models.CharField(max_length=32)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
