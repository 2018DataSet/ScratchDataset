# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-22 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalDataSetModel', '0006_auto_20181122_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(max_length=30)),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalDataSetModel.A')),
            ],
        ),
    ]
