from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tenant, Property,Tenancy_Agreement

# Register your models here.
class TenantAdmin(UserAdmin):
    list_display = ["phone_no", "email", "first_name", "last_name", "is_staff"]
    ordering = ["phone_no"]
    
    fieldsets = (
        (None, {"fields": ("phone_no", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone_no", "email", "first_name", "last_name", "password1", "password2"),
        }),
    )

    def get_username_field(self, request):
        """Force superusers to log in with email"""
        if request.user.is_superuser:
            return "email"
        return "phone_no"
admin.site.register([Tenant,Property,Tenancy_Agreement])

