# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finance',
            name='children',
        ),
    ]
