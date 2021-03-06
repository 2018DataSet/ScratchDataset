# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-22 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalDataSetModel', '0017_processmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processmodel',
            name='operate_object',
            field=models.TextField(blank=True, null=True, verbose_name='操作详情'),
        ),
        migrations.AlterField(
            model_name='processmodel',
            name='operate_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='processmodel',
            name='operate_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='作品ID'),
        ),
        migrations.AlterField(
            model_name='processmodel',
            name='prod_id',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='作品ID'),
        ),
    ]
