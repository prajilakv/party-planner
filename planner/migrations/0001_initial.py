# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('item', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invited',
            fields=[
                ('invited_family', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
        ),
    ]