# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20150304_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultdate',
            name='subject',
        ),
        migrations.AddField(
            model_name='resultdate',
            name='classnumber',
            field=models.ManyToManyField(to='journal.ClassNumber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultdate',
            name='school_year',
            field=models.CharField(default='2014-2015', max_length=100),
            preserve_default=True,
        ),
    ]
