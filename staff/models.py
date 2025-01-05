from django.db import models
from django.urls import reverse

# Create your models here.

class StaffType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=20)
    DOB = models.DateField(blank=False, null=False)
    ID_number = models.CharField(max_length=10)
    staff_type = models.ForeignKey(StaffType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('staff_detail', args=[str(self.id)])
