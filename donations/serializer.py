from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donator', 'donator_id', 'donation_type', 'donation_date', 'donation_amount', 'donation_memo']
        depth = 1
    donator_id = serializers.IntegerField(write_only=True)