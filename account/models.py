from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUserModel(AbstractUser):
    username = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list[str] = ['password']
    EMAIL_FIELD: str = 'email'

    def __str__(self):
        return self.username