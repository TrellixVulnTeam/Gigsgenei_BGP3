# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-23 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bidding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillsneeded',
            name='user',
        ),
        migrations.AlterField(
            model_name='jobsubcatagories',
            name='Catagory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subcatagories', to='Bidding.JobCatagories'),
        ),
        migrations.AlterField(
            model_name='skillsneeded',
            name='JobId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='skillsneeded', to='Bidding.PostJob'),
        ),
    ]
