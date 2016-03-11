# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0004_auto_20160301_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('votes', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]
