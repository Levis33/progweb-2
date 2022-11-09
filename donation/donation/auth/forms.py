from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from project.models import Usuario
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _U
from validate_docbr import CPF

class registerForm(UserCreationForm):
    nome = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'required': 'true'}))
    email = forms.EmailField(label=("email"), max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), error_messages={'required': 'Por favor entre um email válido'})
    cpf = forms.CharField(label='Número do CPF', max_length=14, widget=forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'CPF', 'id': 'cpf'}))
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar senha'}), help_text=("Digite a mesma senha acima, para verificação."))

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')

        if pass1 is not None and pass1 != pass2:
            self.add_error('password2', 'As senhas não correspondem.')

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if Usuario.objects.filter(email=email).count() > 0:
            raise ValidationError(_U('Este email já está associado a um usuário.'))

        return email

    def clean_cpf(self):
        doc_num = self.cleaned_data['cpf']
        doc_teste = doc_num.replace('.', '').replace('/', '').replace('-', '').replace('_', '')

        if not(CPF().validate(doc_teste)):
            raise ValidationError('CPF inválido')
        elif Usuario.objects.filter(cpf=doc_num).exists():
            raise ValidationError('Já existe uma conta cadastrada com esse CPF')
        
        return doc_num

# fazer form criacao de usuario tipo administrador


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = 'Senha'
        self.fields['username'].label = 'Usuário ou E-mail'

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'id_username', 'required': 'true'}), error_messages={'required': 'Por favor entre um email válido'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha', 'id': 'id_password'}))


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'id_email', 'required': 'trure'}), error_messages={'required': 'Email deve ser preenchido'})


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Senha antiga'
        self.fields['new_password1'].label = 'Nova senha'
        self.fields['new_password2'].label = 'Confirmar nova senha'

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'id_old_password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha', 'id': 'id_new_password_1'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar senha', 'id': 'id_new_password_2'}))
