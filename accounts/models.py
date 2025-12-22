from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    
    class Role(models.TextChoices):

        ADMIN = 'ADMIN', 'Admin'
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'

    role = models.CharField(
        max_length=25,
        choices=Role.choices,
        default=Role.STUDENT

        )
    @property
    def is_admin(self) -> bool:
        return self.role == self.Role.ADMIN
    
    @property
    def is_teacher(self) -> bool:
        return self.role ==self.Role.TEACHER
    
    @property
    def is_student(self) -> bool:
        return self.role == self.Role.STUDENT
    
    groups = models.ManyToManyField(
        Group,
        related_name='+', 
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='+', 
        blank=True,
        help_text='Specific permissions for this user.'
    )

