from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'is_superuser', 'last_login']

class RegisterSerializer(serializers.ModelSerializer):

    confirm = serializers.CharField(max_length = 128)
    class Meta:
        model = User 
        fields = ['username', 'password', 'confirm', 'email', 'first_name', 'last_name']

    def validate(self, attrs):
        if attrs['password']!= attrs['confirm']:
            raise serializers.ValidationError('Password bilan confirm mos emas!')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        
        user.save()

        return user
