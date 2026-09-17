from rest_framework import serializers
from .models import FoodOrder

class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrder
        fields = '__all__'
