# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0017_auto_20171102_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='city',
            field=models.CharField(default='Sri City', max_length=100),
        ),
    ]
