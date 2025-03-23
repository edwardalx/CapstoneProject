from django.db import models
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class Tenant(AbstractUser):
    phone_no = models.CharField(max_length=11, primary_key=True, blank=False, unique= True)
    
    USERNAME_FIELD = "phone_no"
    REQUIRED_FIELDS = ["first_name","last_name","email"]

class Property(models.Model):
    name = models.CharField(max_length=200, blank=False, null= False, unique= True)
    location = models.CharField(max_length=200, blank=False, null= False)
    no_of_units = models.IntegerField(max_length=3, blank=True, null= True)
    cost_of_rent = models.IntegerField(max_length=10, blank=True, null= True)
    availability = models.IntegerField(max_length=1, blank=False, null= False)


class Tenancy_Agreement(models.Model):
    contract_start_date = models.DateField(blank=False, null= False)
    contract_duration = models.IntegerField(help_text="Duration in months")
    contact_end_date = models.DateField(blank=True, null= True)
    phone_no = models.ManyToManyField(Tenant, related_name='tenancy_agreement')
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='tenancy_agreement')
    room_number = models.CharField(max_length=14, blank=False, null= False)




    def save(self, *args, **kwargs):
        if self.contract_start_date and self.contract_duration:
            self.contact_end_date = self.contract_start_date + relativedelta(months=self.contract_duration)
        super().save(*args,**kwargs)

