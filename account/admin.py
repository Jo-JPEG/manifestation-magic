from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'display_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'display_name'),
        }),
    )
    list_display = ('username', 'email', 'display_name', 'is_staff')
    search_fields = ('username', 'email', 'display_name')
    ordering = ('username',)
    readonly_fields = ('date_joined',)  # Add this line to make date_joined read-only

admin.site.register(CustomUser, UserAdmin)


