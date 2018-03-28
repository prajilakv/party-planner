# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_auto_20170925_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='guests',
            name='status',
            field=models.CharField(choices=[('1', 'To invite'), ('2', 'Invited'), ('3', 'Confirmed'), ('4', 'Waiting'), ('5', 'Not Coming')], default='1', max_length=6),
        ),
    ]