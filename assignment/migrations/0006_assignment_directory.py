# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-13 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0005_assestment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='directory',
            field=models.CharField(default='NA', max_length=500),
        ),
    ]
