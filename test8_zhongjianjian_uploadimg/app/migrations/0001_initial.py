# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-15 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('icon', models.FileField(upload_to='upload')),
            ],
        ),
    ]
