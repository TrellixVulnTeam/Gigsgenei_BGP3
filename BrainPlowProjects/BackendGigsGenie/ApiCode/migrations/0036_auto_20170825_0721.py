# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0035_auto_20170824_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institutename',
            name='Name',
        ),
        migrations.AddField(
            model_name='institutename',
            name='alpha_two_code',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='institutename',
            name='country',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='institutename',
            name='domain',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='institutename',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='institutename',
            name='web_page',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
