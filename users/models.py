from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    username = models.CharField(max_length=13, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def token(self):
        return RefreshToken.for_user(self)