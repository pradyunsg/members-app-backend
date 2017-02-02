# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiserv', '0003_auto_20170201_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mem_type',
            field=models.CharField(choices=[(0, 'UNPAID'), (1, 'PAID'), (2, 'CREDIT')], default=0, max_length=12),
        ),
    ]
