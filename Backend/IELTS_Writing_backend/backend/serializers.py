from rest_framework import serializers
from .models import Acedamic_Writing_Task1, General_Writing_Task1, Academic_General_Writing_Task2


class Acedamic_Writing_Task1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Acedamic_Writing_Task1
        fields = '__all__'


class General_Writing_Task1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = General_Writing_Task1
        fields = '__all__'


class Academic_General_Writing_Task2_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_General_Writing_Task2
        fields = '__all__'