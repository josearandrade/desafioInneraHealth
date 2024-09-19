from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AnswerPSQI, FormPSQI, CustomUser

admin.site.register(FormPSQI)
admin.site.register(AnswerPSQI)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date',)}), 
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_date',)}),
    )
    list_display = ['username', 'email', 'birth_date', 'is_staff', 'is_active']
