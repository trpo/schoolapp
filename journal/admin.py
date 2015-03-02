from django.contrib import admin

# Register your models here.
from .models import subject, class_of_students, record, user_privileges

"""
class SubjectInline(admin.TabularInline):
    model = subject
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



admin.site.register(subject, SubjectAdmin)

admin.site.register(class_of_students)
admin.site.register(record)
admin.site.register(user_privileges)