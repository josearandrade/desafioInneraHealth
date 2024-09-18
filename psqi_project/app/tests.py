from django.test import TestCase
from django.utils import timezone
from .models import CustomUser, FormularioPSQI, RespostaPSQI
from .forms import RespostaPSQIForm

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            password='12345', 
            data_nascimento='1990-01-01'
        )

    def test_user_creation(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.data_nascimento, timezone.datetime(1990, 1, 1).date())

class FormularioPSQITestCase(TestCase):
    def setUp(self):
        self.formulario = FormularioPSQI.objects.create()

    def test_formulario_creation(self):
        formulario = FormularioPSQI.objects.get(pk=self.formulario.pk)
        self.assertEqual(formulario.titulo, 'Questionário PSQI')
        self.assertEqual(formulario.descricao, 'Por favor, responda às perguntas abaixo para avaliar a qualidade do seu sono.')

class RespostaPSQITestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            password='12345', 
            data_nascimento='1990-01-01'
        )
        self.formulario = FormularioPSQI.objects.create()
        self.resposta = RespostaPSQI.objects.create(
            usuario=self.user,
            formulario=self.formulario,
            pergunta_1=22,
            pergunta_2=15,
            pergunta_3=6,
            pergunta_4=6,
            pergunta_5a=1,
            pergunta_5b=0,
            pergunta_5c=0,
            pergunta_5d=0,
            pergunta_5e=0,
            pergunta_5f=0,
            pergunta_5g=0,
            pergunta_5h=0,
            pergunta_5i=0,
            pergunta_5ja='',
            pergunta_5jb=0,
            pergunta_6=1,
            pergunta_7=0,
            pergunta_8=0,
            pergunta_9=0,
            pergunta_10=0,
        )

    def test_calcular_pontuacao_item_2(self):
        """Testa o cálculo do item 2"""
        pontuacao = self.resposta.calcular_pontuacao_item_2()
        print('\nitem 2')
        print(pontuacao)
        self.assertEqual(pontuacao, 0)

    def test_calcular_pontuacao_item_3(self):
        """Testa o cálculo do item 3"""
        pontuacao = self.resposta.calcular_pontuacao_item_3()
        print('\nitem 3')
        print(pontuacao)
        self.assertEqual(pontuacao, 1)

    def test_calcular_pontuacao_item_4(self):
        """Testa o cálculo do item 4"""
        pontuacao = self.resposta.calcular_pontuacao_item_4()
        print('\nitem 4')
        print(pontuacao)
        self.assertEqual(pontuacao, 3)  # Teste baseado na eficiência do sono

    def test_calcular_pontuacao_item_5(self):
        """Testa o cálculo do item 5"""
        pontuacao = self.resposta.calcular_pontuacao_item_5()
        print('\nitem 5')
        print(pontuacao)
        self.assertEqual(pontuacao, 1)  # Nenhum distúrbio de sono

    def test_calcular_pontuacao_item_7(self):
        """Testa o cálculo do item 5"""
        pontuacao = self.resposta.calcular_pontuacao_item_7()
        print('\nitem 7')
        print(pontuacao)
        self.assertEqual(pontuacao, 0)  # Nenhum distúrbio de sono

    def test_calcular_pontuacao_total(self):
        """Testa o cálculo da pontuação total"""
        pontuacao_total = self.resposta.calcular_pontuacao_total()
        print('\ntotal')
        self.assertEqual(pontuacao_total, 7)  # Exemplo de pontuação total

class RespostaPSQIFormTestCase(TestCase):
    def test_form_validation(self):
        """Testa a validação do formulário"""
        data = {
            'pergunta_1': 22,
            'pergunta_2': 15,
            'pergunta_3': 6,
            'pergunta_4': 6,
            'pergunta_5a': 1,
            'pergunta_5b': 0,
            'pergunta_5c': 0,
            'pergunta_5d': 0,
            'pergunta_5e': 0,
            'pergunta_5f': 0,
            'pergunta_5g': 0,
            'pergunta_5h': 0,
            'pergunta_5i': 0,
            'pergunta_5ja': '',
            'pergunta_5jb': 0,
            'pergunta_6': 1,
            'pergunta_7': 0,
            'pergunta_8': 0,
            'pergunta_9': 0,
            'pergunta_10': 0,
        }
        form = RespostaPSQIForm(data)
        
