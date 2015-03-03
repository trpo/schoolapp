from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

SCORE_CHOICES = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
    )

ATTENDANCE_CHOICES = (
    ('P', 'Присутвовал'),
    ('B', 'Болеет'),
    ('N', 'Не был на уроке'),
    ('O', 'Освобожден')
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

LEVEL_CHOICES = (
    ('STD', 'Ученик'),
    ('TEA', 'Учитель'),
    ('DIR', 'Директор')
    )

SEX_CHOICES = (
    ('Men', 'Муж.'),
    ('Wmn', 'Жен.')
    )



class Subject(models.Model):
    name_subject = models.CharField(max_length=100)
    hours_per_qarter = models.IntegerField(default=8)

    def __str__(self):
        return "{0}".format(self.name_subject)

    def get_absolute_url(self):
        return "/journal/%i/" % self.id


class ClassNumber(models.Model):
    letter = models.CharField(max_length=3, default='1А')

    def __str__(self):
        return "{0}".format(self.letter)


class Student (User):
    access_level =  models.CharField(max_length=3, default='STD', choices=LEVEL_CHOICES)
    student_manager = models.CharField(max_length=3, default='STD', choices=STUDENT_MANAGER_CHOICES)
    sex  = models.CharField(max_length=4, default='Муж.', choices=SEX_CHOICES)

    classnumber = models.ForeignKey(ClassNumber)

    objects = UserManager()

#    def __str__(self):
#        return "{0}".format(self.name)

class Teacher (User):
    access_level =  models.CharField(max_length=3, default='TEA', choices=LEVEL_CHOICES)
    teacher_manager = models.CharField(max_length=3, default='TEA', choices=TEACHER_MANAGER_CHOICES)

    classnumber = models.ForeignKey(ClassNumber)

    objects = UserManager()

#    def __str__(self):
#        return "{0}".format(self.name)


class Record(models.Model):
    date_record = models.DateTimeField('Дата')
    theme = models.CharField(max_length=300)
    hometask = models.CharField(max_length=300)

    teacher = models.ForeignKey(Teacher)
    class_number = models.ForeignKey(ClassNumber)
    subject = models.ForeignKey(Subject, related_name="subject_of_record")

    def __str__(self):
        return "{0} {1}".format(self.subject, self.date_record)


class Evaluation(models.Model):
    score = models.CharField(max_length=1, default='5', choices=SCORE_CHOICES)
    attendance = models.CharField(max_length=1, default='P', choices=ATTENDANCE_CHOICES)
    comment = models.CharField(max_length=300)

    record = models.ForeignKey(Record)
    student = models.ForeignKey(Student, related_name="score_of_student")

    def __str__(self):
        return "{0} оценка {1} урок {2}".format(self.student, self.score, self.record)


