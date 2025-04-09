from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AlreadyRegistered
from .models import CustomUser

# Si ya estaba registrado, lo desregistramos primero
try:
    admin.site.unregister(CustomUser)
except admin.sites.NotRegistered:
    pass

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email','first_name','last_name','role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol Personalizado', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol Personalizado', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

