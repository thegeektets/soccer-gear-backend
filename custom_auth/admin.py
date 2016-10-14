from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _

# Define a new User admin
from django.contrib.auth.admin import UserAdmin

from custom_auth.models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_admin','mobile_number',
    	'default_billing_address', 'default_shipping_address', 'mpesa_phone_number', 'password', 'last_login', 'date_joined'
                    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','full_name', 'email','mobile_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions','is_admin')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Address Fields'), {'fields': ('default_billing_address', 'default_shipping_address')}),
        (_('Payment Details'), {'fields': ('mpesa_phone_number',)}),
    )

# Re-register UserAdmin
admin.site.register(User, UserAdmin)
