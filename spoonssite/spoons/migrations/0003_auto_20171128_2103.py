# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 02:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spoons', '0002_auto_20171128_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]