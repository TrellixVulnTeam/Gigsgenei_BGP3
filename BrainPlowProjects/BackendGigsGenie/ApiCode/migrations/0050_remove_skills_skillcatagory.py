# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-16 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0049_auto_20171013_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='SkillCatagory',
        ),
    ]
