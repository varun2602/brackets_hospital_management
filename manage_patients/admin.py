from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


# Register your models here.
class AuthuserView(admin.ModelAdmin):
    list_display = ['username', 'is_active', 'is_superuser']
    list_filter = ['is_active', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class PatientView(admin.ModelAdmin):
    list_display = ['PatientID', 'username', 'email', 'company_name', 'company_designation', 'insurance']


admin.site.register(models.Authuser, AuthuserView)
admin.site.register(models.Patient, PatientView)
