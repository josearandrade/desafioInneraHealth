# desafioInnera
Aplicação feita para o desafio de implementação Innera Health

# Documentação de Requisitos

## 1. Introdução

Esta documentação descreve os requisitos para o desenvolvimento de uma aplicação web que permita ao usuário preencher o Questionário de Qualidade do Sono de Pittsburgh (PSQI) e visualizar os resultados de forma organizada.

## 2. Objetivo

Desenvolver uma aplicação web interativa para o preenchimento e análise do PSQI, fornecendo uma interface intuitiva para o usuário, validação dos dados inseridos, exibição de resultados e armazenamento das respostas para consulta futura.

## 3. Requisitos Funcionais

### 3.1. Interface do Questionário PSQI

- **Descrição:** A aplicação deve apresentar uma página web com todas as perguntas do PSQI conforme o PDF fornecido.
- **Detalhes:**
  - **Perguntas:** Reproduzir todas as perguntas do questionário de maneira fiel.
  - **Tipos de Respostas:**
    - **Múltipla Escolha:** Permitir seleção entre opções predefinidas.
    - **Escalas:** Permitir seleção de valores dentro de uma escala (por exemplo, 0 a 3).
    - **Texto Livre:** Campos para respostas em texto livre (e.g., horas dormidas, tempo para adormecer).

### 3.2. Validação de Dados

- **Descrição:** Garantir a integridade e a validade dos dados inseridos pelo usuário.
- **Detalhes:**
  - **Perguntas Obrigatórias:** Verificar se todas as perguntas obrigatórias foram respondidas antes de permitir o envio do formulário.
  - **Validações Específicas:**
    - **Valores Numéricos:** Assegurar que respostas numéricas (e.g., horas e minutos) estejam dentro de intervalos válidos.
    - **Escalas:** Verificar se as respostas em escala estão dentro dos valores permitidos.

### 3.3. Resultados

- **Descrição:** Após o envio do questionário, redirecionar o usuário para uma página de resultados.
- **Detalhes:**
  - **Exibição de Respostas:** Mostrar todas as respostas fornecidas pelo usuário.
  - **Cálculo da Pontuação:** Calcular e exibir a pontuação total do PSQI.
  - **Explicação da Pontuação:** Fornecer uma breve explicação sobre o que a pontuação indica, incluindo a interpretação clínica (por exemplo, o que uma pontuação acima de um determinado valor representa em termos de qualidade do sono).

### 3.4. Armazenamento de Dados

- **Descrição:** Salvar as respostas do questionário e permitir a visualização do histórico.
- **Detalhes:**
  - **Formato de Armazenamento:** Utilizar um banco de dados simples, como SQLite, ou um arquivo JSON para armazenar as respostas.
  - **Histórico de Respostas:** Implementar uma funcionalidade que permita ao usuário visualizar e comparar seu histórico de respostas ao longo do tempo.

## 4. Requisitos Não Funcionais

### 4.1. Tecnologias

- **Back-End:**
  - **Opções:** Python (Flask ou Django) ou Node.js.
- **Front-End:**
  - **Opções:** HTML/CSS/JavaScript, ou frameworks como React.

### 4.2. Interface Responsiva

- **Descrição:** A aplicação deve ter uma interface responsiva que funcione adequadamente em dispositivos móveis.

### 4.3. Experiência do Usuário

- **Descrição:** Garantir uma experiência de usuário intuitiva e eficiente, especialmente para o preenchimento de respostas em texto livre.

### 4.4. Visualização Gráfica (Extras Desejáveis)

- **Descrição:** Utilizar ferramentas como Chart.js ou Plotly para exibir visualizações gráficas das pontuações anteriores.

### 4.5. Autenticação Simples (Extras Desejáveis)

- **Descrição:** Implementar um sistema de login para permitir que os usuários salvem e acessem seus questionários e resultados.a
