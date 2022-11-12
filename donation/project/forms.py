from django import forms
from django.contrib.auth.models import User
from project.models import Usuario, Campanha
from django.core.exceptions import ValidationError

escolhas = ((True, "Ativado"), (False, "Desativado"))
ufs = (('RO', 'RO'), ('AC', 'AC'), ('AM', 'AM'), ('RR', 'RR'), ('PA', 'PA'), ('AP', 'AP'), ('TO', 'TO'), ('MA', 'MA'), ('PI', 'PI'), ('CE', 'CE'), ('RN', 'RN'), ('PB', 'PB'), ('PE', 'PE'), ('AL', 'AL'), ('SE', 'SE'), ('BA', 'BA'), ('MG', 'MG'), ('ES', 'ES'), ('RJ', 'RJ'), ('SP', 'SP'), ('PR', 'PR'), ('SC', 'SC'), ('RS', 'RS'), ('MS', 'MS'), ('MT', 'MT'), ('GO', 'GO'), ('DF', 'DF'))

class EditGerenciaUsuarioForm(forms.Form):
    is_active = forms.ChoiceField(choices=escolhas, widget=forms.Select(attrs={'class': 'form-select'}), required=True)

    class Meta:
        model = Usuario
        fields = ['is_active']


class CriarCampanhaForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do evento de Doação', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_nome_evento'}))
    data_inicio = forms.DateField(label='Data de Início', required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'campo_data_inicio'}))
    data_fim = forms.DateField(label='Data de Fim', required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'campo_data_fim'}))
    CEP = forms.CharField(label='CEP', max_length=8, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_cep'}))
    uf = forms.CharField(label="Estado", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_uf'}))
    cidade = forms.CharField(label='Cidade', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_cidade'}))
    bairro = forms.CharField(label='Bairro', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_bairro'}))
    rua = forms.CharField(label='Rua', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_rua'}))
    valor_necessario = forms.DecimalField(label='Valor Necessário', required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'campo_valor_necessario'}))
    descricao = forms.CharField(label='Descrição', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'campo_descricao'}))
    foto = forms.ImageField(label='Foto', required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'campo_foto'}))
    # finalizado = forms.BooleanField(label="Finalizar Evento", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'campo_finalizar_evento'}))

    class Meta:
        model = Campanha
        fields = ['nome', 'data_inicio', 'data_fim', 'CEP', 'uf', 'cidade', 'bairro', 'rua', 'valor_necessario', 'descricao', 'foto']

    def clean_data_ida(self):
        data_ida = self.cleaned_data['data_ida']
        data_volta = self.cleaned_data['data_fim']
        if data_ida > data_volta:
            raise ValidationError("A data de início precisa ser antes da data de finalização")
        return self.cleaned_data['data_ida']
    
    def clean_valor_necessario(self):
        valor = self.cleaned_data['valor_necessario']
        if valor < 1:
            raise ValidationError('Esse valor é muito baixo, por favor coloque um valor maior')
        return valor