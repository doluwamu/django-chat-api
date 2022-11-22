from django.db import models
from account.models import BaseUserModel

class MessageModel(models.Model):
    user = models.ForeignKey(BaseUserModel, on_delete=models.CASCADE)
    receiver = models.ForeignKey(BaseUserModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="received_messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__ (self):
        return self.message
