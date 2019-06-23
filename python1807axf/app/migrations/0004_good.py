# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-17 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productimg', models.CharField(max_length=256)),
                ('productname', models.CharField(max_length=256)),
                ('productlongname', models.CharField(max_length=256)),
                ('isxf', models.IntegerField(max_length=256)),
                ('pmdesc', models.IntegerField(max_length=256)),
                ('specifics', models.CharField(max_length=256)),
                ('price', models.FloatField(max_length=256)),
                ('marketprice', models.FloatField(max_length=256)),
                ('categoryid', models.IntegerField(max_length=256)),
                ('childcid', models.IntegerField(max_length=256)),
                ('childcidname', models.CharField(max_length=256)),
                ('dealerid', models.CharField(max_length=256)),
                ('storenums', models.IntegerField(max_length=256)),
                ('productnum', models.IntegerField(max_length=256)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]