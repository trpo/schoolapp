from django.contrib import admin

# Register your models here.
from journal.models import Subject, Record, Student, Teacher, ClassNumber, Evaluation 

"""
class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

"""

class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name_subject']}),
        ('Количество часов в четверти', {'fields': ['hours_per_qarter']}),
    ]

    list_display = ('name_subject', 'hours_per_qarter')
    list_filter = ['hours_per_qarter', 'name_subject']
    search_fields = ['name_subject']

    #inlines = [SubjectInline]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Record)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ClassNumber)
admin.site.register(Evaluation)
