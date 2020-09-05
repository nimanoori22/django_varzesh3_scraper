from django.contrib import admin
from .models import MyNewsFb
# Register your models here.

class MyNewsFbAdmin(admin.ModelAdmin):
    list_display = ('title', 'mytime', 'mydate')


admin.site.register(MyNewsFb, MyNewsFbAdmin)
