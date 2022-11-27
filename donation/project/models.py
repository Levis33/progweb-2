from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

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

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField(max_length=200)
    CEP = models.CharField(max_length=9)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    finalizado = models.BooleanField(default=False)
    valor_necessario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(blank=True, null=True)

class Doacao(models.Model):
    id = models.AutoField(primary_key=True)
    id_campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    email = models.EmailField('email_address')
    cc_number = CardNumberField('card number')
    cc_expiry = CardExpiryField('expiration date')
    cc_code = SecurityCodeField('security code')
    nome_cartao = models.CharField(max_length=50)
    cpf_titular = models.CharField(max_length=14)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)


class MensagemFAQ(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField('email_address')
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
