from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tenant, Property,Tenancy_Agreement

# Register your models here.
class TenantAdmin(UserAdmin):
    list_display = ["phone_no", "email", "first_name", "last_name", "is_staff"]
    ordering = ["phone_no"]

admin.site.register([Tenant,Property,Tenancy_Agreement])

