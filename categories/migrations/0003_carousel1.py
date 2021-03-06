# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-24 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20161024_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='carousel_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount', models.CharField(max_length=5)),
            ],
        ),
    ]
