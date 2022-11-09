from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
class Usuario(AbstractUser):
    email = models.EmailField('email_address', unique=True)
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14)
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf']


class Campanha(models.Model):
    STATUS = (
        ('A', 'Ativo'),
        ('F', 'Finalizado'),
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    CEP = models.CharField(max_length=9)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS)
    valor_necessario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.BinaryField(blank=True, null=True, editable=True)

class Doacao(models.Model):
    id = models.AutoField(primary_key=True)
    id_campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
