# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 20:20
from __future__ import unicode_literals

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_search_vector'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='blog_post_search__528e75_gin'),
        ),
    ]
