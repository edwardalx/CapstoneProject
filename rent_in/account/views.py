from django.shortcuts import render,redirect
from django.views import generic
from .models import Tenant
from django.contrib.auth import views
from django.contrib.auth import login, logout,authenticate
from .forms import TenantForm,TenantLoginForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class RentInHome(generic.TemplateView):
    template_name ='account/base.html'


class RentInRegisterVIew(generic.CreateView):
    form_class = TenantForm
    template_name = 'account/register.html'
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

    return render(request, "account/register.html", {"form": form})

class TenantLoginView(views.LoginView):
    form_class = TenantLoginForm
    template_name ='registration/login.html'
    success_url = reverse_lazy('home')

def tenant_login_view(request):
    if request.method == "POST":
        form = TenantLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Use phone_no as username
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage or dashboard
            form = TenantLoginForm()
    else:
        form = TenantLoginForm()

    return render(request, 'registration/login.html', {'form': form})
    