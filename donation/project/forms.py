from django import forms
from django.contrib.auth.models import User
from project.models import Usuario, Campanha
from django.core.exceptions import ValidationError
from datetime import datetime
from validate_docbr import CPF

escolhas = ((True, "Ativado"), (False, "Desativado"))

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
    foto = forms.ImageField(label='Foto', required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'campo_foto'}))
    # finalizado = forms.BooleanField(label="Finalizar Evento", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'campo_finalizar_evento'}))

    class Meta:
        model = Campanha
        fields = ['nome', 'data_inicio', 'data_fim', 'CEP', 'uf', 'cidade', 'bairro', 'rua', 'valor_necessario', 'descricao', 'foto']

    def clean_data_ida(self):
        data_ida = self.cleaned_data['data_ida']
        data_volta = self.cleaned_data['data_fim']
        print('fake')
        if data_ida > data_volta:
            print('testeee')
            raise ValidationError("A data de início precisa ser antes da data de finalização")
        return self.cleaned_data['data_ida']

    def clean_valor_necessario(self):
        valor = self.cleaned_data['valor_necessario']
        if valor < 1:
            raise ValidationError('Esse valor é muito baixo, por favor coloque um valor maior')
        return valor


class EditCampanhaForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do evento de Doação', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_nome_evento'}))
    data_inicio = forms.DateField(label='Data de Início', required=True, widget=forms.DateInput(attrs={ 'class': 'form-control', 'id': 'campo_data_inicio'}))
    data_fim = forms.DateField(label='Data de Fim', required=True, widget=forms.DateInput(attrs={ 'class': 'form-control', 'id': 'campo_data_fim'}))
    CEP = forms.CharField(label='CEP', max_length=8, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_cep'}))
    uf = forms.CharField(label="Estado", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_uf'}))
    cidade = forms.CharField(label='Cidade', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_cidade'}))
    bairro = forms.CharField(label='Bairro', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_bairro'}))
    rua = forms.CharField(label='Rua', max_length=70, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'campo_rua'}))
    valor_necessario = forms.DecimalField(label='Valor Necessário', required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'campo_valor_necessario'}))
    descricao = forms.CharField(label='Descrição', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'campo_descricao'}))
    foto = forms.ImageField(label='Foto', required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'campo_foto'}))
    finalizado = forms.BooleanField(label="Finalizar Evento", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'campo_finalizar_evento'}))

    class Meta:
        model = Campanha
        fields = ['nome', 'data_inicio', 'data_fim', 'CEP', 'uf', 'cidade', 'bairro', 'rua', 'valor_necessario', 'descricao', 'foto', 'finalizado']


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


class DoacaoForm(forms.Form):
    valor = forms.DecimalField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'campo_valor', 'name': 'campo_valor'}))
    email = forms.EmailField(required=True, max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}), error_messages={'required': 'Por favor entre um email válido'})
    cc_number = forms.CharField(max_length=19 ,required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cc_number', 'name': 'campo_cc_number', 'placeholder': "Número do cartão"}))
    cc_expiry = forms.CharField(max_length=5, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cc_expiry', 'name': 'campo_cc_expiry', 'placeholder': "MM/YY"}))
    cc_code = forms.CharField(max_length=4, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cc_code', 'name': 'campo_cc_code',}))
    nome_titular = forms.CharField( required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf_titular = forms.CharField(required=True, max_length=14, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'cpf'}))

    def clean_valor(self):
        valor = self.cleaned_data['valor']
        if valor < 1:
            raise ValidationError('Esse valor é muito baixo, por favor coloque um valor maior')
        return valor

    # nao se salva numero de cartao em banco de dados, logo vamos salvar apenas os 4 ultimos digitos
    def clean_cc_number(self):
        if len(self.cleaned_data['cc_number']) < 16:
            raise ValidationError('Por favor entre um número de cartão válido')
        else:
            cc_number = self.cleaned_data['cc_number'][-4:]
        return cc_number

    def clean_cc_expiry(self):
        today = datetime.today()
        cc_expiry = self.cleaned_data['cc_expiry']
        mes = int(cc_expiry[:2])
        if mes > 12:
            raise ValidationError('Mês inválido')
        cc_expiry = '28/' + cc_expiry
        cc_expiry = datetime.strptime(cc_expiry, '%d/%m/%y')
        if cc_expiry < today:
            raise ValidationError('Essa data já expirou, por favor entre com uma data válida')
        return self.cleaned_data['cc_expiry']

    def clean_cc_code(self):
        cc_code = self.cleaned_data['cc_code']
        return len(cc_code)*'*'

    def clean_cpf_titular(self):
        doc_num = self.cleaned_data['cpf_titular']
        doc_teste = doc_num.replace('.', '').replace('/', '').replace('-', '').replace('_', '')

        if not(CPF().validate(doc_teste)):
            raise ValidationError('CPF inválido')
        return doc_num