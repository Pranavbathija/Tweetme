# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-12 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20190611_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet'),
        ),
    ]