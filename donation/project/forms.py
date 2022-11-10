from django import forms
from django.contrib.auth.models import User
from project.models import Usuario

escolhas = ((True, "Ativado"), (False, "Desativado"))

class EditGerenciaUsuarioForm(forms.Form):
    is_active = forms.ChoiceField(choices=escolhas, widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Usuario
        fields = ['is_active']