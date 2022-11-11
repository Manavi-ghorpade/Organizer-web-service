from django.contrib import admin

# Register your models here.
from tasks.models import Task
from tasks.models import TaskCategory
#Register your models here
admin.site.register(Task)
admin.site.register(TaskCategory)
