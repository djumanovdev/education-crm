from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Student(models.Model):
    account = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="student"
    )
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, unique=True)
    status = models.BooleanField(default=True)
    is_risk = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
