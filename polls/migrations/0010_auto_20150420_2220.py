# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20150420_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 22, 20, 10, 999785, tzinfo=utc), verbose_name=b'time answered')),
                ('answer', models.ForeignKey(to='polls.Answer')),
                ('user', models.ForeignKey(to='polls.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='answer_date',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answer_date',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 22, 20, 10, 997189, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.DeleteModel(
            name='Answer_Date',
        ),
    ]
