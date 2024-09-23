# Desafio de Implementação: Aplicação de Questionário PSQI

## Objetivo
Desenvolver uma aplicação web que permita aos usuários preencher o Questionário de Qualidade do Sono de Pittsburgh (PSQI) e visualizar os resultados de forma organizada.

## Tecnologias Utilizadas
- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap), JS
- **Banco de Dados**: SQLite

## Funcionalidades
1. **Interface do Questionário PSQI**
   - Página para preencher todas as perguntas do PSQI com diferentes tipos de resposta (múltipla escolha, escalas, texto livre).

2. **Validação de Dados**
   - Validações para garantir que todas as perguntas obrigatórias sejam respondidas corretamente.

3. **Resultados**
   - Após o envio do questionário, o usuário é redirecionado para uma página que mostra suas respostas e calcula a pontuação total do PSQI, com explicações sobre o significado da pontuação.

4. **Armazenamento de Dados**
   - Respostas do questionário armazenadas em um banco de dados e visualização do histórico de respostas.

5. **Autenticação**
   - Funcionalidades de registro e login para que os usuários possam salvar e acessar seus próprios questionários e resultados.

## Estrutura do Projeto
- `/psqi_project/`
  - `/app/` - Código fonte da aplicação
  - `/templates/` - Templates HTML
  - `/static/` - Arquivos estáticos (CSS, JS)
  - `manage.py` - Script para gerenciar o projeto Django
- `requirements.txt` - Dependências do projeto

## Como Executar o Projeto

### Pré-requisitos
- Python 3.x
- Django
- Dependências listadas em `requirements.txt`

### Passos para Configuração
1. Clone o repositório:
   ```bash
   git clone https://github.com/josearandrade/desafioInnera.git
   cd psqi_project
2. Crie e ative um virtualenv:
   ```bash
   python3 -m venv venv
No linux:
   ```bash
   source venv/bin/activate
   ```
No windows:
   ```bash
   .venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Execute as migrações:
   ```bash
   python manage.py migrate
4. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver 
5. Acesse a aplicação em http://localhost:8000




# Contato
Para mais informações, entre em contato com joseandrade.work@gmail.com
