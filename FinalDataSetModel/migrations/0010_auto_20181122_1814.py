# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-22 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalDataSetModel', '0009_auto_20181122_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b',
            name='a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalDataSetModel.TeacherModel'),
        ),
    ]
