# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150420_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_loc',
        ),
        migrations.AddField(
            model_name='question',
            name='pub_lat',
            field=models.FloatField(null=True, verbose_name=b'Latitude', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='pub_lon',
            field=models.FloatField(null=True, verbose_name=b'Longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 20, 8, 37, 185553, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
