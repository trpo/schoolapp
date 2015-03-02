# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='class_of_students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('class_number', models.CharField(max_length=2, default='1А')),
                ('student', models.ForeignKey(related_name='students_when_teaching_in_class', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_record', models.DateTimeField(verbose_name='Date')),
                ('score', models.CharField(max_length=1, default='5', choices=[('2', 'Неудовлетворительно'), ('3', 'Удовлетворительно'), ('4', 'Хорошо'), ('5', 'Отлично')])),
                ('attendance', models.CharField(max_length=1, default='P', choices=[('P', 'Присутвовал'), ('B', 'Болеет'), ('N', 'Не был на уроке'), ('O', 'Освобожден')])),
                ('comment', models.CharField(max_length=300)),
                ('students_score', models.ForeignKey(related_name='score_for_student_in_record', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name_subject', models.CharField(max_length=100)),
                ('hours_per_qarter', models.IntegerField(default=18)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user_privileges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('access_level', models.IntegerField(default=0)),
                ('teacher_manager', models.CharField(max_length=20, default='TEA', choices=[('TEA', 'Не имеет классного руководства'), ('MAN', 'Классный руководитель')])),
                ('student_manager', models.CharField(max_length=20, default='STD', choices=[('STD', 'Обычный ученик'), ('ELD', 'Староста класса'), ('WRK', 'Ученик ответственный за трудовой сектор'), ('EDU', 'Ученик ответственный за учебный сектор')])),
                ('class_of_students', models.ForeignKey(to='journal.class_of_students')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='record',
            name='subject_record',
            field=models.ForeignKey(to='journal.subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='teachers_record',
            field=models.ForeignKey(related_name='teacher_who_create_record', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
