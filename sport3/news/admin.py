from django.contrib import admin
from .models import MyNewsFb
# Register your models here.

# class MyNewsFbAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'myurl': ('title', )}

admin.site.register(MyNewsFb)
