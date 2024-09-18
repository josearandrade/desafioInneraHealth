from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, RespostaPSQI

class CustomUserCreationForm(UserCreationForm):
    data_nascimento = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2100)),
        label="Data de nascimento"
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'data_nascimento', 'password1', 'password2')

class RespostaPSQIForm(forms.ModelForm):
    OPCOES = [
        (0, 'Nenhuma'),
        (1, 'Uma'),
        (2, 'Duas'),
        (3, 'Três'),
    ]
    # O tratamento do IntegerField será feito no frontend
    pergunta_1 = forms.IntegerField(label='1 - Quando você geralmente foi para a cama à noite?')
    pergunta_2 = forms.IntegerField(label='2 - Quanto tempo (em minutos) você geralmente levou para dormir à noite?')
    pergunta_3 = forms.IntegerField(label='3 - Quando você geralmente levantou de manhã?')
    pergunta_4 = forms.IntegerField(label='4 - Quantas horas de sono você teve por noite?')
    pergunta_5a = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='A) Não conseguiu adormecer em até 30 minutos')
    pergunta_5b = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='B) Acordou no meio da noite ou de manhã cedo')
    pergunta_5c = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='C) Precisou levantar para ir ao banheiro')
    pergunta_5d = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='D) Não conseguiu respirar confortavelmente')
    pergunta_5e = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='E) Tossiu ou roncou forte')
    pergunta_5f = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='F) Sentiu muito frio')
    pergunta_5g = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='G) Sentiu muito calor')
    pergunta_5h = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='H) Teve sonhos ruins')
    pergunta_5i = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='I) Teve dor')
    pergunta_5ja = forms.CharField(widget=forms.TextInput, label='J) Outra(s) razão(ões), por favor descreva:')
    pergunta_5jb = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='Com que frequência teve dificuldade para dormir devido a essa razão?')
    pergunta_6 = forms.ChoiceField(choices=[(0, 'Muito Boa'), (1, 'Boa'), (2, 'Razoável'), (3, 'Ruim')], widget=forms.RadioSelect, label='6 - Como você avalia sua qualidade geral do sono no último mês?')
    pergunta_7 = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='7 - Com que frequência você tomou medicamento para ajudar a dormir?')
    pergunta_8 = forms.ChoiceField(choices=OPCOES, widget=forms.RadioSelect, label='8 - Com que frequência teve dificuldade para ficar acordado em atividades sociais ou dirigindo?')
    pergunta_9 = forms.ChoiceField(choices=[(0, 'Nenhuma Dificuldade'), (1, 'Um problema leve'), (2, 'Um problema razoável'), (3, 'Um grande problema')], widget=forms.RadioSelect, label='9 - Quão problemático foi manter o ânimo para fazer as coisas habituais?')
    pergunta_10 = forms.ChoiceField(choices=[(0, 'Não'), (1, 'Parceiro ou colega, mas em outro quarto'), (2, 'Parceiro no mesmo quarto, mas em outra cama'), (3, 'Parceiro na mesma cama')], widget=forms.RadioSelect, label='10 - Você tem um parceiro ou colega de quarto?')

    class Meta:
        model = RespostaPSQI
        fields = '__all__'
