# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-19 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkgsearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=100)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pkgsearch.Package')),
            ],
        ),
    ]
