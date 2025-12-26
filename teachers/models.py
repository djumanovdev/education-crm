from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Teacher(models.Model):
    account = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="teacher"
    )
    profession = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
