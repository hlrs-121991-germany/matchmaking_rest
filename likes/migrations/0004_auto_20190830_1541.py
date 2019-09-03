# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-30 15:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0003_auto_20190827_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlike',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]