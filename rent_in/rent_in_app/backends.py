# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Tenant



class PhoneNoBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            tenant = Tenant.objects.get(phone_no=username)  # Use phone_no as username
            if tenant.check_password(password):
                return tenant
        except Tenant.DoesNotExist:
            return None
