# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 19:41
from __future__ import unicode_literals

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]
