from django.contrib import admin
from .models import student
# Register your models here.
class stuadmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'age' , 'course']
admin.site.register(student,stuadmin)