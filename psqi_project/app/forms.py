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
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]
    # O tratamento do IntegerField será feito no frontend
    question_1 = forms.CharField(label='1. Durante o último mês, quando você geralmente foi para a cama a noite?')
    question_2 = forms.IntegerField(label='2. Durante o último mês, quanto tempo (em minutos) você geralmente levou para dormir a noite?')
    question_3 = forms.CharField(label='3. Durante o último mês, quando você geralmente levantou de manhã?')
    question_4 = forms.IntegerField(label='4. Durante o último mês, quantas horas de sono você teve por noite? (Este pode ser diferente do número de horas que você ficou na cama) ')
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
    question_7 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='7. Durante o último mês, com que frequência você tomou medicamento (prescrito ou “por conta própria”) para lhe ajudar a dormir?')
    question_8 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label='8. No último mês, que frequência você teve dificuldade para ficar acordado enquanto dirigia, comia ou participava de uma atividade social (festa, reunião de amigos, trabalho, estudo)')
    question_9 = forms.ChoiceField(choices=[(0, 'Nenhuma Dificuldade'), (1, 'Um problema leve'), (2, 'Um problema razoável'), (3, 'Um grande problema')], widget=forms.RadioSelect, label='9. Durante o último mês, quão problemático foi pra você manter o entusiasmo (ânimo) para fazer as coisas (suas atividades habituais)?')
    question_10 = forms.ChoiceField(choices=[(0, 'Não'), (1, 'Parceiro ou colega, mas em outro quarto'), (2, 'Parceiro no mesmo quarto, mas em outra cama'), (3, 'Parceiro na mesma cama')], widget=forms.RadioSelect, label='10. Você tem um(a) parceiro [esposo (a)] ou colega de quarto?')

    class Meta:
        model = AnswerPSQI
        fields = '__all__'