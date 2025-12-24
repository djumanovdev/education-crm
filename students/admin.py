from django.contrib import admin
from .models import Student,Teacher,Group,Attendance,Payment

admin.site.register([Student,Teacher,Group,Attendance,Payment])