from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import DonatorSerializer
from .models import Donator

# Create your views here.

@api_view(['GET', 'POST'])
def donators_list(request):
    if request.method == 'GET':
        donators = Donator.objects.all()
        serializer = DonatorSerializer(donators, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DonatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)