from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    username = None
    email = models.EmailField('email_address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []