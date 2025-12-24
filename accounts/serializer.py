from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework import status
from .models import CustomUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','groups','user_permissions','is_staff','last_login','is_active']
        

class RegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=128)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
            'confirm',
            'email',
            'last_name',
            'first_name'
        ]
        
    def validate(self, attrs):
        
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('confirm password bilan bir xil emas')
        
        return super().validate(attrs)
        
    
    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    
