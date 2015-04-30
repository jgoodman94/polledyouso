# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150420_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 22, 18, 53, 963577, tzinfo=utc), verbose_name=b'time answered')),
                ('answer', models.ForeignKey(to='polls.Answer')),
                ('user', models.ForeignKey(to='polls.User')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 22, 18, 53, 961393, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
