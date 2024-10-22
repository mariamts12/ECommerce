from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(validators=[MinValueValidator(16)])
