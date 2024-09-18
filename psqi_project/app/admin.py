from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RespostaPSQI, FormularioPSQI, CustomUser

# Register your models here.
admin.site.register(FormularioPSQI)
admin.site.register(RespostaPSQI)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Opcional: customize os campos exibidos no admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('data_nascimento',)}),  # Campos extras
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('data_nascimento',)}),
    )

    # Configura as opções de listagem no painel
    list_display = ['username', 'email', 'data_nascimento', 'is_staff', 'is_active']
