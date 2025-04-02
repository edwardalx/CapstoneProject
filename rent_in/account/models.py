from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group,Permission,BaseUserManager
# Create your models here.
class TenantUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The given phone number must be set")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create a superuser with a phone number (username) and email."""
        if not email:
            raise ValueError("Superusers must have an email address")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        user = self.create_user(username=username, email=self.normalize_email(email), password=password, **extra_fields)
        return user
class Tenant(AbstractUser):
    username = models.CharField(max_length=11, primary_key=True, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=False)
    id_image = models.ImageField(upload_to='properties_images/', blank=True, null=True)
    
    # username = None  # Remove default username
    objects = TenantUserManager()
    
    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"Phone Number: {self.username}  Name: {self.first_name}"