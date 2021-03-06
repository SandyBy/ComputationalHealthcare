# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CH3', '0015_n2group_index_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='N4Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('unlinked_count', models.IntegerField(default=0)),
                ('key', models.CharField(max_length=100)),
                ('filename', models.CharField(default='', max_length=200)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CH3.Dataset')),
            ],
        ),
        migrations.RemoveField(
            model_name='n1entry',
            name='computed',
        ),
        migrations.RemoveField(
            model_name='n1entry',
            name='initialf',
        ),
        migrations.RemoveField(
            model_name='n1entry',
            name='subf',
        ),
        migrations.RemoveField(
            model_name='n1group',
            name='computed',
        ),
        migrations.RemoveField(
            model_name='n2entry',
            name='computed',
        ),
        migrations.RemoveField(
            model_name='n2entry',
            name='initialf',
        ),
        migrations.RemoveField(
            model_name='n2entry',
            name='subf',
        ),
        migrations.RemoveField(
            model_name='n3entry',
            name='computed',
        ),
        migrations.RemoveField(
            model_name='n3entry',
            name='initialf',
        ),
        migrations.RemoveField(
            model_name='n3entry',
            name='subf',
        ),
        migrations.RemoveField(
            model_name='n4entry',
            name='computed',
        ),
        migrations.RemoveField(
            model_name='n4entry',
            name='indexf',
        ),
        migrations.RemoveField(
            model_name='n4entry',
            name='subf',
        ),
    ]
