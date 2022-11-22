from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseUserModel
        fields = ['username', 'email']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = models.BaseUserModel(
            username=validated_data.get('username'),
            email = validated_data.get('email')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        Token.objects.create(user=user)
        return user