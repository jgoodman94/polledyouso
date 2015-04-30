# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20150428_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 0, 27, 42, 124336, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 0, 27, 42, 122168, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
