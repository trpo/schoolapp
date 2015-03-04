# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultDate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, default='1 четверть')),
                ('date_begin', models.DateTimeField(verbose_name='Дата начала')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания')),
                ('subject', models.ForeignKey(to='journal.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='resultdate',
            field=models.ForeignKey(to='journal.ResultDate', default=1),
            preserve_default=False,
        ),
    ]
