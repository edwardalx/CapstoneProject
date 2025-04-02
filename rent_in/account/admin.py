from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tenant

# Register your models here.
class TenantAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]
    ordering = ["username"]

admin.site.register(Tenant, TenantAdmin)