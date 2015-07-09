# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20150703_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(related_name='folder', blank=True, to='notes.Folder', null=True),
            preserve_default=True,
        ),
    ]
