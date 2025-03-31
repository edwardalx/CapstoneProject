from django.contrib import admin
from .models import Tenant, Property,Tenancy_Agreement

# Register your models here.
admin.site.register([Tenant,Property,Tenancy_Agreement])

