from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from project.models import Usuario


class registerForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'required': 'true'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}))
    email = forms.EmailField(label=("email"), max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}), error_messages={'required': 'Por favor entre um email válido'})
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar senha'}), help_text=("Digite a mesma senha acima, para verificação."))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


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
