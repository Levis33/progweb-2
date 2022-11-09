from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField('email_address', unique=True)
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14)
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf']
