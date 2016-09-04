# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Doctor'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_registration.Patient'),
        ),
    ]