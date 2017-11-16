# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-07 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Showcase', '0002_auto_20171104_1048'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GigOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(default=False, max_length=10000)),
                ('Prize', models.IntegerField(default=False)),
                ('Days', models.CharField(default=False, max_length=10000)),
                ('Accepted', models.BooleanField(default=False)),
                ('Completed', models.BooleanField(default=False)),
                ('Deleted', models.BooleanField(default=False)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('GigId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Showcase.Gigs')),
                ('Reciever', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_reciever', to=settings.AUTH_USER_MODEL)),
                ('Sender', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
