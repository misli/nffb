# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 16:41
from __future__ import unicode_literals

from django.db import migrations
import nffb.models


class Migration(migrations.Migration):

    dependencies = [
        ('nffb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundextension',
            name='color',
            field=nffb.models.ColorField(default=b'#ffffff', max_length=10, verbose_name='background color'),
        ),
    ]
