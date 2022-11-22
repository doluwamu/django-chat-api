from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from . import models
from . import serializers

class NoPermissionView(object):
    permission_classes = ()
    authentication_classes = ()


class PermissionView(object):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AuthViewset(
    NoPermissionView,
    GenericViewSet,
    mixins.CreateModelMixin
):
    queryset = models.BaseUserModel.objects.all()
    serializer_class = serializers.BaseUserSerializer

    @action(methods=['POST'], detail = False)
    def login(self, request, *args, **kwargs):
        password = request.data.get('password')
        email = request.data.get('email')
        try:
            user = models.BaseUserModel.objects.get(email=email)
        except models.BaseUserModel.DoesNotExist:
            return Response(
                {"detail": 'Invalid email or password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not user.check_password(password):
            return Response({"detail": 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        data = serializers.BaseUserSerializer(user).data
        data['token'] = user.auth_token.key
        return Response(data)

    
    @action(methods=['POST'], detail=False)
    def signup(self, request, *args, **kwargs):
        self.serializer_class = serializers.SignupSerializer
        return self.create(request, *args, **kwargs)

