# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urnik', '0010_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='objavljen',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='semester',
            name='objavljen',
            field=models.BooleanField(default=False),
        ),
    ]