from django.contrib import admin

# Register your models here.

from task_manager.models import User_Profile, Project, Task, Supervisor, Developer, Dev_Work_Task

admin.site.register(User_Profile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Supervisor)
admin.site.register(Developer)
