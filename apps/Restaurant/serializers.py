from rest_framework import serializers
from .models import CuisineType, Restaurant
from apps.Users.serializers import UserSerializer


class CuisineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuisineType
        fields = ['id', 'name']


class RestaurantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cuisine = CuisineTypeSerializer(read_only=True)
    cuisine_id = serializers.PrimaryKeyRelatedField(queryset=CuisineType.objects.all(), write_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'user', 'name', 'place', 'cuisine', 'cuisine_id']
        
