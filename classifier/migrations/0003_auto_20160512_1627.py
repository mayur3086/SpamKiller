# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_auto_20160510_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtable',
            name='mail',
            field=models.CharField(max_length=50000),
        ),
    ]
