# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0002_auto_20170721_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='Country',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
