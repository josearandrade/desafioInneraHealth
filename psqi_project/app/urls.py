from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #   
    path('', views.index, name='index'),
    path('form_guest/answer/', views.answer_psqi, name='answer_psqi'),

    # Login and logout
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='index'), name='logout'),
    # Register
    path('register/', views.register, name='register'),

    # Password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Dashboard and forms
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/my_forms/', views.my_forms, name='my_forms'),
    path('registration/register_or_login/', views.register_or_login, name='register_or_login'),

    
]
