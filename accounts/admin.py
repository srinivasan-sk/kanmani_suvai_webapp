from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Showing password and other data's displayed
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name' , 'last_name' , 'username' , 'date_joined' , 'last_login' , 'is_active')
    list_display_links = ('email' , 'first_name' , 'last_name')
    readonly_fields = ('date_joined' , 'last_login')
    ordering = ('-date_joined' , )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account , AccountAdmin)
