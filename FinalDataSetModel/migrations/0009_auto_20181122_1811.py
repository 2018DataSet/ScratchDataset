# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-22 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalDataSetModel', '0008_auto_20181122_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel1',
            fields=[
                ('teacher_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='用户名')),
                ('school', models.CharField(blank=True, max_length=50, null=True, verbose_name='学校')),
                ('teach_class', models.CharField(blank=True, max_length=100, null=True, verbose_name='所教班级')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='邮箱')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='手机号')),
                ('course_times', models.IntegerField(blank=True, default=0, null=True, verbose_name='创建课程数')),
                ('contest_times', models.IntegerField(blank=True, default=0, null=True, verbose_name='发起的竞赛数')),
                ('production_evalu', models.TextField(verbose_name='评价记录')),
            ],
            options={
                'db_table': 'DataSet_TeacherModel1',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='b',
            name='a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalDataSetModel.TeacherModel1'),
        ),
    ]
