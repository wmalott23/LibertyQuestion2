from django.db import models
from donators.models import Donator

# Create your models here.

class Donation(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE)
    donation_type = models.CharField(max_length=10)
    donation_date = models.DateField()
    donation_amount = models.IntegerField()
    donation_memo = models.CharField(max_length=255)