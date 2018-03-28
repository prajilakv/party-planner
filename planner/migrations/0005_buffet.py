# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20170928_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buffet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kid_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
