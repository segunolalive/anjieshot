# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160205_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date', '-updated']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
    ]
