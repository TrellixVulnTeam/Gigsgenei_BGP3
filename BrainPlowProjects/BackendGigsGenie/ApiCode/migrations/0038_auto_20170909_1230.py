# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-09 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0037_auto_20170826_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigsimages',
            name='GigId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='ApiCode.Gigs'),
        ),
    ]
