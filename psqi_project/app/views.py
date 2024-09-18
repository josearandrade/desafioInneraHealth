from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RespostaPSQIForm
from .models import FormularioPSQI, RespostaPSQI
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'app/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('index')  # Redireciona para a página inicial ou outra página
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def responder_psqi(request, formulario_id):
    formulario = get_object_or_404(FormularioPSQI, id=formulario_id)
    
    if request.method == 'POST':
        form = RespostaPSQIForm(request.POST)
        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.formulario = formulario
            resposta.usuario = request.user
            resposta.save()
            return redirect('index')  # Redirecionar após salvar a resposta
    else:
        form = RespostaPSQIForm()

    return render(request, 'app/formulario.html', {'form': form, 'formulario': formulario})

@login_required
def lista_formularios(request):
    formularios = Formulario.objects.filter(usuario=request.user)  # Busca os formulários do usuário logado
    return render(request, 'app/lista_formularios.html', {'formularios': formularios})

@login_required
def meus_formularios(request):
    # Busca todos os questionários respondidos pelo usuário autenticado
    formularios_respondidos = RespostaPSQI.objects.filter(usuario=request.user)
    
    # ID do formulário selecionado, se houver
    selected_formulario_id = request.GET.get('formulario_id')
    
    # Obtém o formulário selecionado, se existir
    selected_formulario = None
    if selected_formulario_id:
        selected_formulario = get_object_or_404(RespostaPSQI, id=selected_formulario_id, usuario=request.user)
    
    context = {
        'formularios_respondidos': formularios_respondidos,
        'selected_formulario': selected_formulario,
        'selected_formulario_id': selected_formulario_id,
    }
    
    return render(request, 'app/meus_formularios.html', context)
