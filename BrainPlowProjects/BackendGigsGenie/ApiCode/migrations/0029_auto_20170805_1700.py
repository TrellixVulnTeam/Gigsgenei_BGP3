# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0028_firsttimelogin1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttimelogin1',
            name='Firsttime',
            field=models.BooleanField(default=False),
        ),
    ]
