# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20150703_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(related_name='notes', blank=True, to='notes.Folder', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(related_name='notes', null=True, to='notes.Tag', blank=True),
            preserve_default=True,
        ),
    ]
