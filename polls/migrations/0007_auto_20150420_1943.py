# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150420_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lat',
            field=models.FloatField(null=True, verbose_name=b'Latitude', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lon',
            field=models.FloatField(null=True, verbose_name=b'Longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 19, 43, 7, 283390, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
