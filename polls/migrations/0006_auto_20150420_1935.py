# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150420_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 19, 35, 13, 604182, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
