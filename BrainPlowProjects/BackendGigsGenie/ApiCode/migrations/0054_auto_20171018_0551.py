# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-18 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0053_auto_20171016_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acedamicqualification',
            name='EndYear',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acedamicqualification',
            name='StartYear',
            field=models.DateField(blank=True, null=True),
        ),
    ]