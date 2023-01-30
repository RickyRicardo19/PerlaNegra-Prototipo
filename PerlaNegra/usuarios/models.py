from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    es_admin = models.BooleanField(default=False)
