# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20150421_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_lon',
            new_name='lon',
        ),
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 7, 43, 32, 626089, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 7, 43, 32, 623968, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
