from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import DonationSerializer
from .models import Donation

# Create your views here.

@api_view(['GET', 'POST'])
def donations_list(request):
    if request.method == 'GET':
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DonationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)