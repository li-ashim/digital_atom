from django.contrib import admin

from .models import Mentor, Novice, Task, UsefulMaterial


class NoviceAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'department', 'position', 'mentor')

class MentorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'department', 'position', 'novice')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'deadline', 'novice')

class UsefulAdmin(admin.ModelAdmin):
    list_display = ('material_type', 'department', 'title', 'author', 
                    'date_added')


admin.site.register(Mentor, MentorAdmin)
admin.site.register(Novice, NoviceAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(UsefulMaterial, UsefulAdmin)
