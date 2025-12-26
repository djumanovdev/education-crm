from rest_framework import serializers

from .models import Student


class StudentCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()


class StudentListSerializer(serializers.Serializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        