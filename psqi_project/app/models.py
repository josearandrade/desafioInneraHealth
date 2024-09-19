from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=False)

class FormPSQI(models.Model):
    title = models.CharField(max_length=255, default='Questionário PSQI')
    description= models.TextField(default='Por favor, responda às perguntas abaixo para avaliar a qualidade do seu sono.')

    def __str__(self):
        return self.title

class AnswerPSQI(models.Model):
    form = models.ForeignKey(FormPSQI, on_delete=models.CASCADE, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=False)
    answer_date = models.DateField(default=datetime.date.today, editable=False)

    # questions
    question_1 = models.IntegerField()
    question_2 = models.IntegerField()
    question_3 = models.IntegerField()
    question_4 = models.IntegerField()
    question_5a = models.IntegerField()
    question_5b = models.IntegerField()
    question_5c = models.IntegerField()
    question_5d = models.IntegerField()
    question_5e = models.IntegerField()
    question_5f = models.IntegerField()
    question_5g = models.IntegerField()
    question_5h = models.IntegerField()
    question_5i = models.IntegerField()
    question_5ja = models.TextField()
    question_5jb = models.IntegerField()
    question_6 = models.IntegerField()
    question_7 = models.IntegerField()
    question_8 = models.IntegerField()
    question_9 = models.IntegerField()
    question_10 = models.IntegerField()


    total_score = models.IntegerField(editable=False)

    # Cálculo da pontuação do PSQL

    # Item 1) Qualidade subjetiva do sono:
    # Examine a questão 6 e atribua a pontuação (Não precisa de cálculo)

    # Item 2) Latência do sono:
    # Examine a questão 2 e atribua a pontuação de a seguinte maneira:
    # • ≤ 15 minutos = 0 pontos
    # • 16 a 30 minutos = 1 ponto
    # • 31 a 60 minutos = 2 pontos
    # • > 60 minutos = 3 pontos
    #   
    # Examine a questão 5a e atribua a pontuação da seguinte maneira:
    # • Nenhuma vez = 0 ponto;
    # • Menos de 1 vez/semana = 1 ponto
    # • 1 a 2 vezes/semana = 2 pontos
    # • 2 a 3 vezes/semana = 3 pontos (Não precisa de cálculo)
    def calculate_score_item_2(self):
        self.question_2 = int(self.question_2)
        if self.question_2 <= 15:
            return 0
        elif 16 <= self.question_2 <= 30:
            return 1
        elif 31 <= self.question_2 <= 60:
            return 2
        else:
            return 3

    # 3) Duração do sono
    # Examine questão 4 e atribua a pontuação da seguinte maneira:
    # • > 7 horas = 0 ponto
    # • 6 a 7 horas = 1 ponto
    # • 5 a 6 horas = 2 pontos
    # • < 5 horas = 3 pontos
    def calculate_score_item_3(self):
        if self.question_4 > 7:
            return 0
        elif 6 <= self.question_4 <= 7:
            return 1
        elif 5 <= self.question_4 < 6:
            return 2
        else:
            return 3

    # 4) Eficiência habitual do sono
    # Examine a questão 2 e atribua a pontuação da seguinte maneira:
    # • Escreva o número de horas dormidas (questão 4);
    # • Calcule o número de horas no leito: {horário de levantar (questão 3) – horário de deitar (questão 1)};
    # • Calcule a eficiência do sono: {n° de horas dormidas/n° de horas no leito} x 100 = eficiência do sono (%);

    # Atribua a pontuação do componente 4 (eficiência do sono %) da seguinte maneira:
    # • > 85% = 0 ponto
    # • 75 a 84% = 1 pontos
    # • 65 a 74% = 2 pontos
    # • <65% = 3 pontos

    def calculate_score_item_4(self):
        total = (self.question_4 / (self.question_3 - self.question_1)) * 100
        if total >= 85:
            return 0
        elif 84 >= total >= 75:
            return 1
        elif 74 >= total >= 65:
            return 2
        else:
            return 3
    # 5) Distúrbios do sono
    # Examine as questões de 5b a 5j e atribua a pontuação:
    # • Nenhuma vez = 0 ponto;
    # • Menos de 1 vez/sem = 1 ponto
    # • 1 a 2 vezes/semana = 2 pontos
    # • 3 vezes/sem ou mais = 3 pontos
    # Some a pontuação de 5b a 5j e atribua a pontuação do componente 5 da seguinte forma:
    # • 0 = 0 ponto;
    # • 1 a 9 = 1 pontos
    # • 10 a 18 = 2 pontos
    # • 19 a 27 = 3 pontos

    def calculate_score_item_5(self):
        total = 0
        total += self.question_5a
        total += self.question_5b
        total += self.question_5c
        total += self.question_5d
        total += self.question_5e
        total += self.question_5f
        total += self.question_5g
        total += self.question_5h
        total += self.question_5i
        total += self.question_5jb
        if total == 0:
            return 0
        elif 9 >= total >= 1:
            return 1
        elif 18 >= total >= 10:
            return 2
        else:
            return 3

    # 6) Uso de remédio para dormir 
    # Examine a questão 7 e atribua a pontuação (não precisa de cálculo)

    # 7) Disfunção diurna 
    # Some a pontuação das questões 8 e 9 e atribua a pontuação do componente 7 da seguinte maneira:
    # • 0 = 0 ponto
    # • 1 a 2 = 1 ponto
    # • 3 a 4 = 2 pontos
    # • 5 a 6 = 3 pontos
    def calculate_score_item_7(self):
        total = self.question_8 + self.question_9
        if total == 0:
            return 0
        elif 1 >= total >= 2:
            return 1
        elif 3 >= total >= 4:
            return 2
        else: 
            return 3
            
    # Calcula a pontuação total com base nas respostas.
    def calculate_total_score(self):
        score = 0
        score += self.calculate_score_item_2()
        score += self.calculate_score_item_3()
        score += self.calculate_score_item_4()
        score += self.calculate_score_item_5()
        score += self.calculate_score_item_7()
        score += self.question_5a
        score += self.question_6
        score += self.question_7
        return score

    def __str__(self):
        return f'Resposta de {self.user} para {self.form}'

    def save(self, *args, **kwargs):
        self.total_score = self.calculate_total_score()
        super().save(*args, **kwargs)
