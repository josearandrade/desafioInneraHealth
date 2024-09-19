from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AnswerPSQIForm
from .models import FormPSQI, AnswerPSQI
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'app/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def answer_psqi(request, form_id):
    form_psqi= get_object_or_404(FormPSQI, id=form_id)
    
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

    return render(request, 'app/form.html', {'form': form, 'form': form})

@login_required
def forms_list(request):
    forms = AnswerPSQI.objects.filter(user=request.user) 
    return render(request, 'app/forms_list.html', {'forms': forms})

@login_required
def my_forms(request):
    forms_answered = AnswerPSQI.objects.filter(user=request.user)
    selected_form_id = request.GET.get('form_id')
    selected_form = None
    if selected_form_id:
        selected_form = get_object_or_404(AnswerPSQI, id=selected_form_id, user=request.user)
    
    context = {
        'forms_answered': forms_answered,
        'selected_form': selected_form,
        'selected_form_id': selected_form_id,
    }
    
    return render(request, 'app/my_forms.html', context)
