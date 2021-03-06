# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-24 21:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('filing_date', models.DateTimeField(auto_now_add=True)),
                ('incident_date', models.DateField(default='2016-01-01')),
                ('incident_time', models.TimeField(blank=True)),
                ('incident_type', models.CharField(choices=[('Exclusion', 'Exclusion'), ('Inclusion', 'Inclusion')], max_length=10)),
                ('text_description', models.TextField(default='describe incident detail here', verbose_name='Incident Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('descriptors', models.ManyToManyField(default=1, to='bias_tracker.Descriptor')),
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
            name='subjects',
            field=models.ManyToManyField(default=1, to='bias_tracker.Person'),
        ),
    ]
