from django.shortcuts import render, HttpResponse
from .models import Acedamic_Writing_Task1, General_Writing_Task1, Academic_General_Writing_Task2
from rest_framework import status, viewsets
from .serializers import Acedamic_Writing_Task1_Serializer, General_Writing_Task1_Serializer, Academic_General_Writing_Task2_Serializer

class Acedamic_Writing_Task1_Viewset(viewsets.ModelViewSet):
    queryset = Acedamic_Writing_Task1.objects.all()
    serializer_class = Acedamic_Writing_Task1_Serializer
    http_method_names = ['get', 'head']


class General_Writing_Task1_Viewset(viewsets.ModelViewSet):
    queryset = General_Writing_Task1.objects.all()
    serializer_class = General_Writing_Task1_Serializer
    http_method_names = ['get', 'head']


class Academic_General_Writing_Task2_Viewset(viewsets.ModelViewSet):
    queryset = Academic_General_Writing_Task2.objects.all()
    serializer_class = Academic_General_Writing_Task2_Serializer
    http_method_names = ['get', 'head']