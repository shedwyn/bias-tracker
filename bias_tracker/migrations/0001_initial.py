# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=100, verbose_name='Incident Type Descriptor(s)')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filing_date', models.DateTimeField(verbose_name='Filing Date')),
                ('i_date', models.DateField(verbose_name='Incident Date')),
                ('i_time', models.TimeField(blank=True, verbose_name='Incident Time')),
                ('i_type', models.CharField(choices=[('Exclusion', 'Exclusion'), ('Inclusion', 'Inclusion')], max_length=10, verbose_name='Incident Type')),
                ('text_description', models.TextField(verbose_name='Incident Description')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='incident_as_subjects', to='bias_tracker.Person'),
        ),
        migrations.AddField(
            model_name='incident',
            name='i_descriptors',
            field=models.ManyToManyField(to='bias_tracker.Descriptor', verbose_name='Descriptors of Incident Type'),
        ),
        migrations.AddField(
            model_name='incident',
            name='subjects',
            field=models.ManyToManyField(default=None, related_name='incidents_as_author', to='bias_tracker.Person'),
        ),
    ]
