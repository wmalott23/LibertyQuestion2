from rest_framework import serializers
from .models import Donator

class DonatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donator
        fields = ['id', 'ssn', 'name', 'birth_date', 'ethnicity', 'work_address', 'home_address', 'additional_address', 'work_phone', 'home_phone', 'additional_phone']
        