# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20150428_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerinfo',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='answerinfo',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lon',
        ),
        migrations.AddField(
            model_name='answerinfo',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 13, 57, 45, 571908, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 13, 57, 45, 569096, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
