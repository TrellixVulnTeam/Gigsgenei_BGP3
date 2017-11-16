# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCode', '0033_gigs'),
    ]

    operations = [
        migrations.CreateModel(
            name='GigsFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=1000, null=True)),
                ('Answer', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GigsRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Requirement', models.CharField(max_length=100, null=True)),
                ('IsMandatory', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GigsSearchTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SearchTerms', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='gigs',
            name='Catagory',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gigs',
            name='Complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gigs',
            name='Favourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gigs',
            name='Time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='gigs',
            name='Title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gigssearchterms',
            name='GigId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Gigs'),
        ),
        migrations.AddField(
            model_name='gigssearchterms',
            name='UserName',
            field=models.ForeignKey(db_column='UserName', on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Contractor', to_field='UserName'),
        ),
        migrations.AddField(
            model_name='gigsrequirements',
            name='GigId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Gigs'),
        ),
        migrations.AddField(
            model_name='gigsrequirements',
            name='UserName',
            field=models.ForeignKey(db_column='UserName', on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Contractor', to_field='UserName'),
        ),
        migrations.AddField(
            model_name='gigsfaq',
            name='GigId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Gigs'),
        ),
        migrations.AddField(
            model_name='gigsfaq',
            name='UserName',
            field=models.ForeignKey(db_column='UserName', on_delete=django.db.models.deletion.CASCADE, to='ApiCode.Contractor', to_field='UserName'),
        ),
    ]