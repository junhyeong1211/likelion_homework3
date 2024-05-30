from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        token=Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
    def validate(self, data):
        user=authenticate(**data)
        if user:
            token=Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"Error":"Unable to Login"}
        )