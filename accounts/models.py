from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null = True, on_delete=models.CASCADE,)
    date_of_birth = models.DateField(blank=False, null=False)
    Address_Line_1 = models.CharField(max_length=250, blank=True)
    Address_Line_2 = models.CharField(max_length=250, blank=True)
    Address_City = models.CharField(max_length=250, blank=True)
    Address_Country = models.CharField(max_length=250, blank = True)

    def __str__(self):
        return str(self.user)