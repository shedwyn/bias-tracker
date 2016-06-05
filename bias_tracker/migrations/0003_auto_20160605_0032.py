# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bias_tracker', '0002_auto_20160605_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='filing_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateField(default=datetime.datetime(2016, 6, 5, 0, 32, 29, 835689)),
        ),
    ]