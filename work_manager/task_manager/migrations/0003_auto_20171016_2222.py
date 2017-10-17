# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_auto_20171011_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='importance',
            field=models.IntegerField(blank=True, default=None, verbose_name='Importance'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='name',
            field=models.CharField(error_messages={'invalid': 'Wrong format.', 'required': 'You must type a name !'}, max_length=100, verbose_name='Name'),
        ),
    ]
