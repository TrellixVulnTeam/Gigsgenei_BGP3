# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0030_expressyourself_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expressyourself',
            name='Resume',
            field=models.ImageField(null=True, upload_to='uploaded_media/'),
        ),
    ]
