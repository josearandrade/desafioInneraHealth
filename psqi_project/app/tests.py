from django.test import TestCase
from django.utils import timezone
from .models import CustomUser, FormPSQI, AnswerPSQI
from .forms import AnswerPSQIForm

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            password='12345', 
            birth_date='1990-01-01'
        )

    def test_user_creation(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.birth_date, timezone.datetime(1990, 1, 1).date())

class FormPSQITestCase(TestCase):
    def setUp(self):
        self.form = FormPSQI.objects.create()

    def test_form_creation(self):
        form = FormPSQI.objects.get(pk=self.form.pk)
        self.assertEqual(form.title, 'Questionário PSQI')
        self.assertEqual(form.description, 'Por favor, responda às perguntas abaixo para avaliar a qualidade do seu sono.')

class AnswerPSQITestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            password='12345', 
            birth_date='1990-01-01'
        )
        self.form = FormPSQI.objects.create()
        self.answer = AnswerPSQI.objects.create(
            user=self.user,
            form=self.form,
            question_1=22,
            question_2=15,
            question_3=6,
            question_4=6,
            question_5a=1,
            question_5b=0,
            question_5c=0,
            question_5d=0,
            question_5e=0,
            question_5f=0,
            question_5g=0,
            question_5h=0,
            question_5i=0,
            question_5ja='',
            question_5jb=0,
            question_6=1,
            question_7=0,
            question_8=0,
            question_9=0,
            question_10=0,
        )

    def test_calculate_score_item_2(self):
        score = self.answer.calculate_score_item_2()
        self.assertEqual(score, 0)

    def test_calculate_score_item_3(self):
        score = self.answer.calculate_score_item_3()
        self.assertEqual(score, 1)

    def test_calculate_score_item_4(self):
        score = self.answer.calculate_score_item_4()
        self.assertEqual(score, 3)

    def test_calculate_score_item_5(self):
        score = self.answer.calculate_score_item_5()
        self.assertEqual(score, 1)

    def test_calculate_score_item_7(self):
        score = self.answer.calculate_score_item_7()
        self.assertEqual(score, 0)

    def test_calculate_total_score(self):
        total_score = self.answer.calculate_total_score()
        self.assertEqual(total_score, 7)

