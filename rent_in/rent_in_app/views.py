from django.shortcuts import render,redirect
from django.views import generic
from .models import Tenant, Property
from django.contrib.auth import views
from django.contrib.auth import login, logout,authenticate
from .forms import TenantForm,TenantLoginForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class RentInHome(generic.TemplateView):
    template_name ='rent_in_app/base.html'


class RentInRegisterVIew(generic.CreateView):
    form_class = TenantForm
    template_name = 'rent_in_app/register.html'
    success_url = reverse_lazy('login')
def register_view(request):
    if request.method == "POST":
        form = TenantForm(request.POST, request.FILES)  # Handle file uploads too!
        if form.is_valid():
            tenant = form.save(commit=False)  # Save but don't commit yet
            tenant.set_password(form.cleaned_data['password1'])  # Hash password
            tenant.save()
            login(request, tenant)  # Log the user in after registration
            messages.success(request, "Registration successful!")
            return redirect("home")  # Redirect to home or dashboard
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TenantForm()

    return render(request, "rent_in_app/register.html", {"form": form})

class TenantLoginView(views.LoginView):
    form_class = TenantLoginForm
    template_name ='rent_in_app/login.html'
    success_url = reverse_lazy('home')

def tenant_login_view(request):
    if request.method == "POST":
        form = TenantLoginForm(request, data=request.POST)
        if form.is_valid():
            phone_no = form.cleaned_data.get('phone_no')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=phone_no, password=password)  # Use phone_no as username
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage or dashboard
    else:
        form = TenantLoginForm()

    return render(request, 'rent_in_app/login.html', {'form': form})
    
