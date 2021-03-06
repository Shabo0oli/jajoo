# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 13:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckInDate', models.DateTimeField()),
                ('CheckOutDate', models.DateTimeField()),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], default='Pending', max_length=20)),
                ('Guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField(max_length=200)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CostPerDay', models.IntegerField(default=0)),
                ('Address', models.TextField(max_length=500)),
                ('Location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('Bedroom', models.IntegerField(default=0)),
                ('HasParking', models.BooleanField(default=False)),
                ('HasWifi', models.BooleanField(default=False)),
                ('HasBath', models.BooleanField(default=False)),
                ('HasTv', models.BooleanField(default=False)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('Username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Place'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='Place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Place'),
        ),
    ]
