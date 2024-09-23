from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AnswerPSQIForm, CustomUserCreationForm
from .models import FormPSQI, AnswerPSQI, get_score_message
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
import plotly.graph_objects as go
import pandas as pd

def index(request):
    return render(request, 'home/index.html')

### Auth Views
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            # Check for cached PSQI answers
            psqi_answers = request.session.get('psqi_answers', None)
            if psqi_answers:
                form_psqi = get_object_or_404(FormPSQI, id=1)
                answer_form = AnswerPSQIForm(psqi_answers)
                if answer_form.is_valid():
                    answer = answer_form.save(commit=False)
                    answer.form = form_psqi
                    answer.user = user
                    answer.save()
                # Clear the session after saving answers
                del request.session['psqi_answers']

            return redirect('my_forms')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                # Check for cached PSQI answers
                psqi_answers = request.session.get('psqi_answers', None)
                if psqi_answers:
                    form_psqi = get_object_or_404(FormPSQI, id=1)
                    answer_form = AnswerPSQIForm(psqi_answers)
                    if answer_form.is_valid():
                        answer = answer_form.save(commit=False)
                        answer.form = form_psqi
                        answer.user = user
                        answer.save()
                    # Clear the session after saving answers
                    del request.session['psqi_answers']

                return redirect('my_forms')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os campos.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

### Dashboard Views
@login_required
def dashboard(request):
    user = request.user
    forms_answered = AnswerPSQI.objects.filter(user=user)
    
    user_info = {
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
    }

    scores = AnswerPSQI.objects.filter(user=user).order_by('answer_date')

    questions = [
    'question_1', 
    'question_2', 
    'question_3', 
    'question_4', 
    'question_5a', 
    'question_5b', 
    'question_5c', 
    'question_5d', 
    'question_5e', 
    'question_5f', 
    'question_5g', 
    'question_5h', 
    'question_5i', 
    'question_5ja', 
    'question_5jb', 
    'question_6'
]
    data = list(scores.values(
    'answer_date',
    'total_score',
    'question_1',
    'question_2',
    'question_3',
    'question_4',
    'question_5a',
    'question_5b',
    'question_5c',
    'question_5d',
    'question_5e',
    'question_5f',
    'question_5g',
    'question_5h',
    'question_5i',
    'question_5ja',
    'question_5jb',
    'question_6'
))

    df = pd.DataFrame(data)

    plot_div = None
    if not df.empty:
        fig = go.Figure()
        
        for question in questions:
            fig.add_trace(go.Scatter(
                x=df['answer_date'],
                y=df[question],
                mode='lines+markers',
                name=question,
                visible=False
            ))

        fig.data[0].visible = True

        dropdown_buttons = []
        for i, question in enumerate(questions):
            dropdown_buttons.append({
                'args': [{'visible': [j == i for j in range(len(questions))]}],
                'label': question,
                'method': 'restyle'
            })

        fig.update_layout(
            title='Evolução por Pergunta',
            xaxis_title='Data',
            yaxis_title='Pontuação por Pergunta',
            updatemenus=[{
                'active': 0,
                'buttons': dropdown_buttons,
                'x': 1.15,
                'y': 1.15,
                'xanchor': 'right',
                'yanchor': 'top'
            }]
        )

        plot_div = fig.to_html(full_html=False)

    total_score_plot_div = None
    if not df.empty:
        fig_total = go.Figure()

        marker_colors = ['green' if score <= 5 else 'yellow' if 6 <= score <= 10 else 'red' for score in df['total_score']]

        fig_total.add_trace(go.Scatter(
            x=df['answer_date'],
            y=df['total_score'],
            mode='lines+markers',
            marker=dict(color=marker_colors, size=10)
        ))

        fig_total.update_layout(
            title='PSQI Total Scores',
            xaxis_title='Data',
            yaxis_title='Pontuação Total'
        )
        total_score_plot_div = fig_total.to_html(full_html=False)

    # Get the latest score message
    latest_score = scores.last().total_score if scores.exists() else 0
    score_message = get_score_message(latest_score)

    # Combine all context for rendering the template
    context = {
        'dashboard_data': scores,
        'plot_div': plot_div,
        'total_score_plot_div': total_score_plot_div,
        'user_info': user_info,
        'forms_answered': forms_answered,
        'score_message': score_message,
        'page': 'dashboard',
    }

    return render(request, 'dashboard/dashboard.html', context)

    

### Form Views

def answer_psqi(request):
    form_psqi, created = FormPSQI.objects.get_or_create(id=1)

    # If user is logged in, handle the form normally
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AnswerPSQIForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.form = form_psqi
                answer.user = request.user
                answer.save()
                return redirect('my_forms') 
        else:
            form = AnswerPSQIForm()
        return render(request, 'home/form.html', {'form': form, 'form_psqi': form_psqi})

    # If user is not logged in, store answers temporarily
    else:
        if request.method == 'POST':
            form = AnswerPSQIForm(request.POST)
            if form.is_valid():
                # Store the form data in the session for later
                request.session['psqi_answers'] = request.POST
                return redirect('register')
        else:
            form = AnswerPSQIForm()

        return render(request, 'home/form.html', {'form': form, 'form_psqi': form_psqi})


# View for user registration or login
def register_or_login(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            # Handle registration
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                # Retrieve PSQI answers from the session after registration
                psqi_answers = request.session.get('psqi_answers', None)
                if psqi_answers:
                    form_psqi = get_object_or_404(FormPSQI, id=1)
                    form = AnswerPSQIForm(psqi_answers)
                    if form.is_valid():
                        answer = form.save(commit=False)
                        answer.form = form_psqi
                        answer.user = user
                        answer.save()
                # Redirect to user's dashboard or form history
                return redirect('my_forms')

        elif 'login' in request.POST:
            # Handle login
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                # Retrieve PSQI answers from the session after login
                psqi_answers = request.session.get('psqi_answers', None)
                if psqi_answers:
                    form_psqi = get_object_or_404(FormPSQI, id=1)
                    form = AnswerPSQIForm(psqi_answers)
                    if form.is_valid():
                        answer = form.save(commit=False)
                        answer.form = form_psqi
                        answer.user = user
                        answer.save()
                # Redirect to user's dashboard or form history
                return redirect('my_forms')

    else:
        # Display both login and register forms on the same page
        register_form = CustomUserCreationForm()
        login_form = AuthenticationForm()

    return render(request, 'accounts/register_or_login.html', {
        'register_form': register_form,
        'login_form': login_form
    })

@login_required 
def my_forms(request):
    user = request.user
    forms_answered = AnswerPSQI.objects.filter(user=user).order_by('-answer_date')
    selected_form_id = request.GET.get('form_id')
    
    form_psqi= get_object_or_404(FormPSQI, id=1)    
   
    if not selected_form_id and forms_answered.exists():
        selected_form = forms_answered.first()
        selected_form_id = selected_form.id
    else:
        selected_form = get_object_or_404(AnswerPSQI, id=selected_form_id, user=user) if selected_form_id else None

    latest_score = selected_form.total_score if selected_form else 0 
    score_message = get_score_message(latest_score)

    question_labels = [
        '1. Durante o último mês, quando você geralmente foi para a cama a noite?',
        '2. Durante o último mês, quanto tempo (em minutos) você geralmente levou para dormir a noite?',
        '3. Durante o último mês, quando você geralmente levantou de manhã?',
        '4. Durante o último mês, quantas horas de sono você teve por noite? (Este pode ser diferente do número de horas que você ficou na cama)',
        'A) Não conseguiu adormecer em até 30 minutos',
        'B) Acordou no meio da noite ou de manhã cedo',
        'C) Precisou levantar para ir ao banheiro',
        'D) Não conseguiu respirar confortavelmente',
        'E) Tossiu ou roncou forte',
        'F) Sentiu muito frio',
        'G) Sentiu muito calor',
        'H) Teve sonhos ruins',
        'I) Teve dor',
        'Ja) Outra(s) razão(ões), por favor descreva:',
        'Jb) Com que frequência, durante o último mês, você teve dificuldade para dormir devido a essa razão?',
        '6 - Como você avalia sua qualidade geral do sono no último mês?',
        '7. Durante o último mês, com que frequência você tomou medicamento (prescrito ou “por conta própria”) para lhe ajudar a dormir?',
        '8. No último mês, que frequência você teve dificuldade para ficar acordado enquanto dirigia, comia ou participava de uma atividade social (festa, reunião de amigos, trabalho, estudo)',
        '9. Durante o último mês, quão problemático foi pra você manter o entusiasmo (ânimo) para fazer as coisas (suas atividades habituais)?',
        '10. Você tem um(a) parceiro [esposo (a)] ou colega de quarto?'
    ]

    context = {
        'forms_answered': forms_answered,
        'selected_form': selected_form,
        'selected_form_id': selected_form_id,
        'score_message': score_message,
        'form_psqi': form_psqi,
        'question_labels': question_labels,
        'page': 'my_forms',
    }

    return render(request, 'dashboard/my_forms.html', context)




    

