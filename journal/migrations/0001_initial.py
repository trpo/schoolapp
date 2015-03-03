# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('letter', models.CharField(default='1А', max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('score', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1)),
                ('attendance', models.CharField(choices=[('P', 'Присутвовал'), ('B', 'Болеет'), ('N', 'Не был на уроке'), ('O', 'Освобожден')], default='P', max_length=1)),
                ('comment', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_record', models.DateTimeField(verbose_name='Дата')),
                ('theme', models.CharField(max_length=300)),
                ('hometask', models.CharField(max_length=300)),
                ('class_number', models.ForeignKey(to='journal.ClassNumber')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('access_level', models.CharField(choices=[('STD', 'Ученик'), ('TEA', 'Учитель'), ('DIR', 'Директор')], default='STD', max_length=3)),
                ('student_manager', models.CharField(choices=[('STD', 'Обычный ученик'), ('ELD', 'Староста класса'), ('WRK', 'Ученик ответственный за трудовой сектор'), ('EDU', 'Ученик ответственный за учебный сектор')], default='STD', max_length=3)),
                ('sex', models.CharField(choices=[('Men', 'Муж.'), ('Wmn', 'Жен.')], default='Муж.', max_length=4)),
                ('classnumber', models.ForeignKey(to='journal.ClassNumber')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name_subject', models.CharField(max_length=100)),
                ('hours_per_qarter', models.IntegerField(default=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('access_level', models.CharField(choices=[('STD', 'Ученик'), ('TEA', 'Учитель'), ('DIR', 'Директор')], default='TEA', max_length=3)),
                ('teacher_manager', models.CharField(choices=[('TEA', 'Не имеет классного руководства'), ('MAN', 'Классный руководитель')], default='TEA', max_length=3)),
                ('classnumber', models.ForeignKey(to='journal.ClassNumber')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='record',
            name='subject',
            field=models.ForeignKey(to='journal.Subject', related_name='subject_of_record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='teacher',
            field=models.ForeignKey(to='journal.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evaluation',
            name='record',
            field=models.ForeignKey(to='journal.Record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evaluation',
            name='student',
            field=models.ForeignKey(to='journal.Student', related_name='score_of_student'),
            preserve_default=True,
        ),
    ]
