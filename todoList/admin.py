from django.contrib import admin
from .models import *
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'title', 'completed')


# Register your models here.
admin.site.register(TodoItem, TaskAdmin)
