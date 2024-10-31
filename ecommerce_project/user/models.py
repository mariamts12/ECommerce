from django.contrib.auth.models import AbstractUser

# from django.core.validators import MinValueValidator
from django.db import models

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    # age = models.IntegerField(null=True, validators=[MinValueValidator(16)])
    last_active_datetime = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()
