# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-19 05:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ApiCode', '0056_auto_20171019_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='UserName',
        ),
        migrations.AddField(
            model_name='contractor',
            name='Role',
            field=models.CharField(choices=[('A', 'Admin'), ('U', 'User')], default='U', max_length=1),
        ),
        migrations.AddField(
            model_name='contractor',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]