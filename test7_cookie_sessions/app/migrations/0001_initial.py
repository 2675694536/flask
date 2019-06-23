# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-14 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=15)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Room')),
            ],
        ),
    ]
