from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, AnswerPSQI

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2100)),
        label="Data de nascimento"
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'birth_date', 'password1', 'password2')

class AnswerPSQIForm(forms.ModelForm):
    OPTIONS = [
        (0, 'Nenhuma'),
        (1, 'Uma'),
        (2, 'Duas'),
        (3, 'Três'),
    ]
    # O tratamento do IntegerField será feito no frontend
    question_1 = forms.IntegerField(label='1 - Quando você geralmente foi para a cama à noite?')
    question_2 = forms.IntegerField(label='2 - Quanto tempo (em minutos) você geralmente levou para dormir à noite?')
    question_3 = forms.IntegerField(label='3 - Quando você geralmente levantou de manhã?')
    question_4 = forms.IntegerField(label='4 - Quantas horas de sono você teve por noite?')
    question_5a = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='A) Não conseguiu adormecer em até 30 minutos')
    question_5b = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='B) Acordou no meio da noite ou de manhã cedo')
    question_5c = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='C) Precisou levantar para ir ao banheiro')
    question_5d = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='D) Não conseguiu respirar confortavelmente')
    question_5e = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='E) Tossiu ou roncou forte')
    question_5f = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='F) Sentiu muito frio')
    question_5g = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='G) Sentiu muito calor')
    question_5h = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='H) Teve sonhos ruins')
    question_5i = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='I) Teve dor')
    question_5ja = forms.CharField(widget=forms.TextInput, label='J) Outra(s) razão(ões), por favor descreva:')
    question_5jb = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='Com que frequência teve dificuldade para dormir devido a essa razão?')
    question_6 = forms.ChoiceField(choices=[(0, 'Muito Boa'), (1, 'Boa'), (2, 'Razoável'), (3, 'Ruim')], widget=forms.RadioSelect, label='6 - Como você avalia sua qualidade geral do sono no último mês?')
    question_7 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='7 - Com que frequência você tomou medicamento para ajudar a dormir?')
    question_8 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='8 - Com que frequência teve dificuldade para ficar acordado em atividades sociais ou dirigindo?')
    question_9 = forms.ChoiceField(choices=[(0, 'Nenhuma Dificuldade'), (1, 'Um problema leve'), (2, 'Um problema razoável'), (3, 'Um grande problema')], widget=forms.RadioSelect, label='9 - Quão problemático foi manter o ânimo para fazer as coisas habituais?')
    question_10 = forms.ChoiceField(choices=[(0, 'Não'), (1, 'Parceiro ou colega, mas em outro quarto'), (2, 'Parceiro no mesmo quarto, mas em outra cama'), (3, 'Parceiro na mesma cama')], widget=forms.RadioSelect, label='10 - Você tem um parceiro ou colega de quarto?')

    class Meta:
        model = AnswerPSQI
        fields = '__all__'