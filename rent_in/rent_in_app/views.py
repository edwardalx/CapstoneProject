from django.shortcuts import render
from django.views import generic
from .models import Tenant, Property
# Create your views here.

class RentInHome(generic.TemplateView):
    template_name ='rent_in_app/base.html'
    
    
