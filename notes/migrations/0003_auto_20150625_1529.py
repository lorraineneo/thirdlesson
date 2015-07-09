# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150621_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'purple', max_length=6, blank=True)),
                ('fontcolor', models.CharField(default=b'white', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'red', max_length=6, blank=True)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(default=b'yellow', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 15, 28, 44, 835600, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 15, 28, 56, 925535, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(related_name='folder', default='', blank=True, to='notes.Folder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='notes.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
