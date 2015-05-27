# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_wil', '0002_auto_20150527_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tardy',
            name='tardy_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 10, 50, 49, 54568, tzinfo=utc)),
        ),
    ]
