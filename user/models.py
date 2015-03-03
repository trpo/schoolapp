from django.db import models
#from django.contrib.auth.models import User
#from journal.models import Subject, Lesson, ResultDate, ClassNumber, Record

# Create your models here.

"""
STUDENT_MANAGER_CHOICES = (
    ('STD', 'Обычный ученик'),
    ('ELD', 'Староста класса'),
    ('WRK', 'Ученик ответственный за трудовой сектор'),
    ('EDU', 'Ученик ответственный за учебный сектор')
    )


SEX_CHOICES = (
    ('Men', 'Муж.'),
    ('Wmn', 'Жен.')
    )



class Student (models.Model):
    name  = models.CharField(max_length=300)
    last_name  = models.CharField(max_length=300)
    middle_name  = models.CharField(max_length=300)
    sex  = models.CharField(max_length=4, default='Муж.', choices=SEX_CHOICES)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    classnumber = models.ForeignKey(ClassNumber)
    student_manager = models.CharField(max_length=20, default='STD', choices=STUDENT_MANAGER_CHOICES)

    access_level =  models.IntegerField(default=0)
    teacher_manager = models.CharField(max_length=20, default='TEA', choices=TEACHER_MANAGER_CHOICES)
    class_of_students =  models.ForeignKey(class_of_students)
    user = models.ForeignKey(User, related_name="user with some privilege")


class Teacher(models.Model):
    name  = models.CharField(max_length=300)
    last_name  = models.CharField(max_length=300)
    middle_name  = models.CharField(max_length=300)
    subject = models.ForeignKey(Subject)
    classnumber = models.ForeignKey(ClassNumber, verbose_name = u"Проводит занятия", related_name="teach_class")
    classnumber = models.ForeignKey(ClassNumber, verbose_name = u"Классный руководитель", related_name="manage_class")

"""