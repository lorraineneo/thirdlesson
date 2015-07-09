# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20150703_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 59, 14, 212715, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folder',
            name='color',
            field=models.CharField(default=b'purple', max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 1, 59, 27, 548049, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='due',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(default=b'red', max_length=6),
            preserve_default=True,
        ),
    ]
