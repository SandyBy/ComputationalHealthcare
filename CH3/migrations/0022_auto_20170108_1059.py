# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CH3', '0021_textsearch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textsearch',
            name='total_count',
        ),
        migrations.AddField(
            model_name='textsearch',
            name='code_type',
            field=models.CharField(default='', max_length=5),
        ),
    ]
