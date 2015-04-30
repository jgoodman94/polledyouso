# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20150429_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='flags',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 2, 4, 21, 282336, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 2, 4, 21, 278891, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
