# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-07 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('technology', models.CharField(max_length=100)),
            ],
        ),
    ]
