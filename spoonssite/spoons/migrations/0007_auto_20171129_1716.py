# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoons', '0006_auto_20171129_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spoontask',
            name='task',
            field=models.CharField(max_length=20),
        ),
    ]
