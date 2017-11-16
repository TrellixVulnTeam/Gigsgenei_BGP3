# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-11 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0045_auto_20171010_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 10, 11, 11, 32, 7, 846522, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='Status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='BidOwner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bidowner', to='ApiCode.Contractor', to_field='UserName'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='Bidder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='ApiCode.Contractor', to_field='UserName'),
        ),
    ]