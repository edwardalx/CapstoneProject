
from django.urls import path
from .views import RentInHome,RentInRegisterVIew
from django.contrib.auth import views

urlpatterns=[
    path('', view=RentInHome.as_view(), name='home'),
    path('login/', view=views.LoginView.as_view(template_name = 'rent_in_app/login.html'), name='login'),
    path('register/', view=RentInRegisterVIew.as_view(), name='register' )
]