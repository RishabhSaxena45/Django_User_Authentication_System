from django.contrib import admin
from .models import userdetails , filedetails
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display = ['id' , 'username' , 'password']
class fileadmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'file']
admin.site.register(userdetails , useradmin)
admin.site.register(filedetails , fileadmin)