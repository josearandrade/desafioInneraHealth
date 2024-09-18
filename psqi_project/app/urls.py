from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Login e logout usando as views prontas do Django
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # View para registro de usuários
    path('register/', views.register, name='register'),

    # Formularios
    path('formulario/<int:formulario_id>/responder/', views.responder_psqi, name='responder_psqi'),
    path('lista_formulario/', views.lista_formularios, name='lista_formularios'),
    path('meus-formularios/', views.meus_formularios, name='meus_formularios'),
    # ... outras rotas
]
