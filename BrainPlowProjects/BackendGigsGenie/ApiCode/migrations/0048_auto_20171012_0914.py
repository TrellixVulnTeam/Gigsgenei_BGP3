# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-12 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0047_auto_20171011_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='ExpertGuarantee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bid',
            name='HighlightMyBid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bid',
            name='SponsorMyBid',
            field=models.BooleanField(default=False),
        ),
    ]
