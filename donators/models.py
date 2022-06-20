from django.db import models

# Create your models here.

class Donator(models.Model):
    ssn = models.IntegerField()
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    ethnicity = models.CharField(max_length=25)
    work_address = models.CharField(max_length=255)
    home_address = models.CharField(max_length=255)
    additional_address = models.CharField(max_length=255)
    work_phone = models.IntegerField()
    home_phone = models.IntegerField()
    additional_phone = models.IntegerField()
