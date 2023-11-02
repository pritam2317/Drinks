from rest_framework import serializers
from .models import Drink

class Drinkserializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'Description']
