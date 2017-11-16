# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0023_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acedamicqualification',
            name='UserName',
            field=models.ForeignKey(db_column='UserName', on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Contractor', to_field='UserName'),
        ),
    ]