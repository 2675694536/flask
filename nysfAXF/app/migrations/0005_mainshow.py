# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-27 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=100)),
                ('categoryid', models.CharField(max_length=10)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=100)),
                ('childcid1', models.CharField(max_length=10)),
                ('productid1', models.CharField(max_length=10)),
                ('longname1', models.CharField(max_length=50)),
                ('price1', models.CharField(max_length=10)),
                ('marketprice1', models.CharField(max_length=10)),
                ('img2', models.CharField(max_length=100)),
                ('childcid2', models.CharField(max_length=10)),
                ('productid2', models.CharField(max_length=10)),
                ('longname2', models.CharField(max_length=50)),
                ('price2', models.CharField(max_length=10)),
                ('marketprice2', models.CharField(max_length=10)),
                ('img3', models.CharField(max_length=100)),
                ('childcid3', models.CharField(max_length=10)),
                ('productid3', models.CharField(max_length=10)),
                ('longname3', models.CharField(max_length=50)),
                ('price3', models.CharField(max_length=10)),
                ('marketprice3', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]
