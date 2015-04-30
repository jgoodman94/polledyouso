# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20150430_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 14, 1, 17, 849828, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(related_name='question_created', to='polls.User', null=True),
        ),
        migrations.RemoveField(
            model_name='question',
            name='flags',
        ),
        migrations.AddField(
            model_name='question',
            name='flags',
            field=models.ManyToManyField(related_name='question_flagged', to='polls.User', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 30, 14, 1, 17, 845735, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
