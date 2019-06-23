# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-18 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_good'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=256)),
                ('mail', models.CharField(max_length=64)),
                ('sex', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
    ]
