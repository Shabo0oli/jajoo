# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170629_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Avatar',
            field=models.ImageField(upload_to='web/static/avatar/'),
        ),
    ]
