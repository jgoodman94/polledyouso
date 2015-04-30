# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20150422_0743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('question_text',)},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.AlterField(
            model_name='answerinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 8, 59, 29, 810615, tzinfo=utc), verbose_name=b'time answered'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 8, 59, 29, 808495, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
