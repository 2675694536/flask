# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-17 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('img', models.CharField(max_length=256)),
                ('categoryid', models.IntegerField()),
                ('brandname', models.CharField(max_length=128)),
                ('img1', models.CharField(max_length=256)),
                ('childcid1', models.IntegerField()),
                ('productid1', models.IntegerField()),
                ('longname1', models.CharField(max_length=128)),
                ('price1', models.CharField(max_length=54)),
                ('marketprice1', models.CharField(max_length=54)),
                ('img2', models.CharField(max_length=256)),
                ('childcid2', models.IntegerField()),
                ('productid2', models.IntegerField()),
                ('longname2', models.CharField(max_length=256)),
                ('price2', models.CharField(max_length=32)),
                ('marketprice2', models.CharField(max_length=36)),
                ('img3', models.CharField(max_length=256)),
                ('childcid3', models.IntegerField()),
                ('productid3', models.IntegerField()),
                ('longname3', models.CharField(max_length=256)),
                ('price3', models.CharField(max_length=32)),
                ('marketprice3', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]