from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tenant, Property

class TenantForm(UserCreationForm):
    phone_no = forms.CharField(required=True, min_length=5)
    id_image = forms.ImageField(required=False)
    first_name =forms.CharField(required=True, max_length=200)
    last_name = forms.CharField(required=True, max_length=200)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = Tenant
        fields = ['phone_no','id_image','first_name','last_name','email']
