from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # Login and logout
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Register
    path('register/', views.register, name='register'),

    # Forms
    path('form/<int:form_id>/answer/', views.answer_psqi, name='answer_psqi'),
    path('forms_list/', views.forms_list, name='forms_list'),
    path('my_forms/', views.my_forms, name='my_forms'),
]
