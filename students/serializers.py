from rest_framework import serializers

from accounts.models import CustomUser
from .models import Student


class StudentCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'status', 'is_risk', 'created_at', 'updated_at']


class UserStudentDetailSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role', 'email', 'student']
