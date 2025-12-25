from rest_framework import serializers

from .models import Student


class StudentCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()


class StudentListserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentGetOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "full_name",
            "phone_number",
            "status",
            "is_risk",
            "created_at",
            "updated_at",
            "account",
        ]


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
