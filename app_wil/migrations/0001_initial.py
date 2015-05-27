# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tardy',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tardy_datetime', models.DateTimeField(default=datetime.datetime(2015, 5, 27, 10, 41, 40, 685086, tzinfo=utc))),
                ('period', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('excuse', models.CharField(choices=[('Appointment', 'Appointment'), ('Dentist Appointment', 'Dentist Appointment'), ('Dr. Appointment', 'Dr. Appointment'), ('Holiday', 'Holiday'), ('Testing', 'Testing'), ('Family', 'Family'), ('Meeting', 'Meeting'), ("Meeting At Child's School", "Meeting At Child's School"), ('Missed The Bus', 'Missed The Bus'), ('Sick (Headache, etc.)', 'Sick (Headache, etc.)'), ('Work', 'Work'), ('Other', 'Other')], max_length=100)),
                ('note', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tardies',
            },
        ),
    ]
