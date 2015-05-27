# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app_wil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tardy',
            name='tardy_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 10, 47, 13, 485589, tzinfo=utc)),
        ),
    ]
