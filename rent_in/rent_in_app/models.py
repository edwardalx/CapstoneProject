
from django.db import models
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User,AbstractUser,BaseUserManager

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
    
    def __str__(self):
        return f"Tenant:{self.phone_no.first_name} Contract End: {self.contact_end_date}'Amount Left:{self.amount_left}"



class Payment(models.Model):
    phone_no = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payments')
    tenancy_agreement = models.ForeignKey(Tenancy_Agreement, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.IntegerField(blank=True, null=True)
    amount_left = models.IntegerField(blank=True, null=True)
    total_amount_paid = models.IntegerField(blank=True, null=True)
    first_payment_date = models.DateField(auto_now=True)
    last_payment_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount_paid = self.tenancy_agreement.payments.aggregate(models.Sum('amount_paid'))['amount_paid__sum']
        self.amount_left =  self.tenancy_agreement.room_number.cost - self.total_amount_paid 
        super().save(*args, **kwargs)
        # Update the Tenancy_Agreement's amount_paid after saving the payment
       
        self.tenancy_agreement.total_amount_paid = self.total_amount_paid 
        self.tenancy_agreement.save()
    def __str__(self):
        return f"{self.phone_no.first_name} Amount Paid: {self.amount_paid} 'Amount Left:{self.amount_left}"


