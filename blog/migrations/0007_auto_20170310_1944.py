# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170310_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
