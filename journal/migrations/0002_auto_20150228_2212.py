# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date_record',
            field=models.DateTimeField(verbose_name='Дата'),
            preserve_default=True,
        ),
    ]
