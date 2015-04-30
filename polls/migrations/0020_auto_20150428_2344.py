# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20150428_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 23, 44, 24, 198385, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 23, 44, 24, 196122, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
