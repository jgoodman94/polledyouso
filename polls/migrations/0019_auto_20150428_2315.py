# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20150428_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answerinfo',
            old_name='coords',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='coords',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='coords',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 23, 14, 58, 923732, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 23, 14, 58, 920911, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
