# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-16 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0052_auto_20171016_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='EndYear',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='StartYear',
            field=models.DateField(null=True),
        ),
    ]
