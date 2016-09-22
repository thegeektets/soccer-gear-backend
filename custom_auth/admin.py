from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

# Define a new User admin
from django.contrib.auth.admin import UserAdmin

from custom_auth.models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_admin','default_billing', 'address_id', 'shipping_address_id', 'mpesa_id', 'password', 'last_login', 'date_joined'
                    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# Re-register UserAdmin
admin.site.register(User)
