from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SCORE_CHOICES = (
    ('2', 'Неудовлетворительно'),
    ('3', 'Удовлетворительно'),
    ('4', 'Хорошо'),
    ('5', 'Отлично')
    )

ATTENDANCE_CHOICES = (
    ('P', 'Присутвовал'),
    ('B', 'Болеет'),
    ('N', 'Не был на уроке'),
    ('O', 'Освобожден')
    )

"""
CLASS_NUMBER_CHOICES = (
    ('1A', '1A класс'),
    ('5A', '5А класс'),
    ('8A', '8А класс'),
    ('8B', '8Б класс')
    )
"""

LEVEL_CHOICES = (
    ('STD', 'Ученик'),
    ('TEA', 'Учитель'),
    ('DIR', 'Директор')
    )

TEACHER_MANAGER_CHOICES = (
    ('TEA', 'Не имеет классного руководства'),
    ('MAN', 'Классный руководитель')
    )

STUDENT_MANAGER_CHOICES = (
    ('STD', 'Обычный ученик'),
    ('ELD', 'Староста класса'),
    ('WRK', 'Ученик ответственный за трудовой сектор'),
    ('EDU', 'Ученик ответственный за учебный сектор')
    )

class subject(models.Model):
    name_subject = models.CharField(max_length=100)
    hours_per_qarter = models.IntegerField(default=18)


    def __str__(self):
        return "{0}".format(self.name_subject)

    def get_absolute_url(self):
        return "/journal/%i/" % self.id



class class_of_students(models.Model):
    class_number = models.CharField(max_length=2, default='1А')
    student = models.ForeignKey(User, related_name="students_when_teaching_in_class")

    def __str__(self):
        return "{0}".format(self.class_number)

class record(models.Model):
    date_record = models.DateTimeField('Дата')
    score = models.CharField(max_length=1, default='5', choices=SCORE_CHOICES)
    attendance = models.CharField(max_length=1, default='P', choices=ATTENDANCE_CHOICES)
    comment = models.CharField(max_length=300)
    students_score = models.ForeignKey(User, related_name="score_for_student_in_record")
    teachers_record = models.ForeignKey(User, related_name="teacher_who_create_record")
    subject_record = models.ForeignKey(subject)

    def __str__(self):
        return "{0} {1} {2}".format(self.students_score, self.date_record, self.subject_record)

class user_privileges(models.Model):
    access_level =  models.IntegerField(default=0)
    teacher_manager = models.CharField(max_length=20, default='TEA', choices=TEACHER_MANAGER_CHOICES)
    student_manager = models.CharField(max_length=20, default='STD', choices=STUDENT_MANAGER_CHOICES)
    class_of_students =  models.ForeignKey(class_of_students)






