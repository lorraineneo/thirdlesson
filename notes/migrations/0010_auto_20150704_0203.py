# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20150704_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='color',
            field=models.CharField(default=b'purple', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(default=b'red', max_length=50),
            preserve_default=True,
        ),
    ]
