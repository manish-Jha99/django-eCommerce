# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-20 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='abc', unique=True),
        ),
    ]
