from django.contrib import admin
from .models import Tenant,Property

# Register your models here.
admin.site.register([Tenant,Property])
