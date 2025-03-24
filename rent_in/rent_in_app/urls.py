from django.urls import path
from .views import RentInHome

urlpatterns=[
    path('', view=RentInHome.as_view(), name='home'),
    ]