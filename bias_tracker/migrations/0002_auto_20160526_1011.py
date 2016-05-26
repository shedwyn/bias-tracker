# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bias_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident_as_subjects', to='bias_tracker.Person'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='subjects',
            field=models.ManyToManyField(related_name='incidents_as_author', to='bias_tracker.Person'),
        ),
    ]
