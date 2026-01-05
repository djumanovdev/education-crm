from django.contrib import admin

from .models import Group, Attendance


admin.site.register([Group, Attendance])
