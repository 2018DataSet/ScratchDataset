# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-22 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalDataSetModel', '0003_knowmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowModel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.IntegerField(unique=True, verbose_name='课程编号')),
                ('chapter_id', models.IntegerField()),
                ('name', models.CharField(max_length=50, verbose_name='知识点名称')),
                ('content', models.TextField(verbose_name='知识点内容')),
                ('audio', models.CharField(blank=True, max_length=100, null=True, verbose_name='音频描述')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'db_table': 'DataSet_KnowModel_chapter',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='knowmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='knowmodel',
            name='lesson_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='课程编号'),
        ),
        migrations.AlterUniqueTogether(
            name='knowmodel1',
            unique_together=set([('lesson_id', 'chapter_id')]),
        ),
    ]
