# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20150625_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.AlterField(
            model_name='folder',
            name='fontcolor',
            field=models.CharField(default=b'white', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(blank=True, to='notes.Folder', null=True),
            preserve_default=True,
        ),
    ]
