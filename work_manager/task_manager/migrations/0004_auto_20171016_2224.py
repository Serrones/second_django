# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_auto_20171016_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.IntegerField(verbose_name='Importance'),
        ),
    ]
