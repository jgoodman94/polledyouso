# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('text',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('text',)},
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='pub_loc',
            field=models.CharField(max_length=40, verbose_name=b'location', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to='polls.User'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='users',
            field=models.ManyToManyField(to='polls.User', blank=True),
        ),
    ]
