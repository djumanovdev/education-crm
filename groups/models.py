from django.db import models

from teachers.models import Teacher
from students.models import Student


class Group(models.Model):
    class Status(models.TextChoices):
        PLANNED = "PLANNED", "Rejada"
        ACTIVE = "ACTIVE", "O'qiyapti"
        STOPPED = "STOPPED", "To'tatilgan"
        FINISHED = "GRATUATED", "Bititirgan"
        CANCELED = "CANCELED", "Bekor qilingan"

    name = models.CharField(unique=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.DO_NOTHING, related_name="groups"
    )
    students = models.ManyToManyField(Student, related_name="groups")
    status = models.CharField(choices=Status.choices, default=Status.PLANNED)

    start_date = models.DateField()
    end_date = models.DateField()


class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "PRESENT", "Keldi"
        ABSENT = "ABSENT", "Kemagan"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, default=Status.PRESENT)
    date = models.DateField()
