from rest_framework import serializers
from . import models
from account.serializers import BaseUserSerializer

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MessageModel
        read_only_fields = ('id', 'created_at',)
        fields = ['id', 'created_at', 'receiver', 'message']

    def validate(self, data):
        user = self.context['request'].user
        print("User", user)
        print("Data", data)
        if user.id == data['receiver'].id:
            raise serializers.ValidationError({'receiver': "You cannot send a message to yourself"})
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        data = validated_data
        data.update(**{"user": user})
        print(data)
        return super().create(data)


class MessageSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer()
    receiver = BaseUserSerializer()

    class Meta:
        model = models.MessageModel
        read_only_fields = ('created_at',)
        fields = "__all__"