from django.db import models
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User,AbstractUser,Group,Permission,BaseUserManager



# Create your models here.
class TenantUserManager(BaseUserManager):
         use_in_migrations = True
         def create_user(self, phone_no,username=None, password=None, **extra_fields):
                if not email:
                    raise ValueError("The given username must be set")
                email = self.normalize_email(phone_no)
                extra_fields.setdefault("is_staff", False)
                extra_fields.setdefault("is_superuser", False)
                user = self.model(phone_no=phone_no, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
class Tenant(AbstractUser):
    phone_no = models.CharField(max_length=11, primary_key=True, blank=False, unique= True)
    username = None


    objects=TenantUserManager()
    USERNAME_FIELD = "phone_no"
    REQUIRED_FIELDS = ["first_name","last_name","email"]
    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)

    def __str__(self):
        return f"Phone Number: {self.phone_no}  Name: {self.first_name}"


class Property(models.Model):
    name = models.CharField(max_length=200, blank=False, null= False, unique= True)
    location = models.CharField(max_length=200, blank=False, null= False)
    no_of_units = models.IntegerField(blank=True, null= True)
    cost_of_rent = models.IntegerField(blank=True, null= True)
    availability = models.BooleanField(blank=False, null= False)

    def __str__(self):
        return f"Property: {self.name} Average Cost of a Room: {self.cost_of_rent} "


class Tenancy_Agreement(models.Model):
    contract_start_date = models.DateField(blank=False, null= False)
    contract_duration = models.IntegerField(help_text="Duration in months")
    contact_end_date = models.DateField(blank=True, null= True)
    phone_no = models.ManyToManyField(Tenant, related_name='tenancy_agreement')
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='tenancy_agreement')
    room_number = models.CharField(max_length=14, blank=False, null= False)

    def __str__(self):
        return f"Property Name: {self.property_name}  Start: {self.contract_start_date }  End: {self.contact_end_date}"




    def save(self, *args, **kwargs):
        if self.contract_start_date and self.contract_duration:
            self.contact_end_date = self.contract_start_date + relativedelta(months=self.contract_duration)
        super().save(*args,**kwargs)

