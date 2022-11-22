from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
import django_filters.rest_framework

from account.views import PermissionView
from . import models, serializers
import json

class MessageViewset(
    PermissionView,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = models.MessageModel.objects.all()
    serializer_class = serializers.MessageSerializer
    search = [
        'message', 'user__username', 'receiver__username'
    ]
    filter_backends = [
        filters.SearchFilter,
        django_filters.rest_framework.DjangoFilterBackend
    ]
    filterset_fields = [
        'user__id',
        'receiver__id'
    ]

    def create(self, request, *args, **kwargs):
        self.serializer_class = serializers.CreateMessageSerializer
        response: Response = super().create(request, *args, **kwargs)
        if (response.status_code != status.HTTP_201_CREATED):
            return response
        print(response.data, type(response.data))
        return Response(
            data=serializers.MessageSerializer(models.MessageModel.objects.get(id=response.data.get('id'))).data,
            status=response.status_code
        )

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=request.user)
        return super().list(request, *args, **kwargs)
