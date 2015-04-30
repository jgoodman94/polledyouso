# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20150420_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(null=True, verbose_name=b'Latitude', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name=b'Longitude', blank=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 2, 5, 29, 125592, tzinfo=utc), verbose_name=b'time answered')),
                ('answer', models.ForeignKey(to='polls.Answer')),
                ('user', models.ForeignKey(to='polls.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='answerdate',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answerdate',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 2, 5, 29, 122510, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.DeleteModel(
            name='AnswerDate',
        ),
    ]
