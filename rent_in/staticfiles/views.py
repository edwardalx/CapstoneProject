from django.shortcuts import render
from django.views import generic
from .models import Tenant, Property
from django.contrib.auth import views
from .forms import TenantForm
from django.urls import reverse_lazy
# Create your views here.

class RentInHome(generic.TemplateView):
    template_name ='rent_in_app/base.html'


class RentInRegisterVIew(generic.CreateView):
    form_class = TenantForm
    template_name = 'rent_in_app/register.html'
    success_url = reverse_lazy('login')

    
    
