# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150410_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(to='polls.User', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=0),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 19, 33, 49, 775017, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
