from rest_framework import serializers
from .models import Visit
from apps.Restaurant.serializers import RestaurantSerializer
from apps.Restaurant.models import Restaurant


class VisitListSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), write_only=True)

    class Meta:
        model = Visit
        fields = ['id', 'restaurant', 'visit_date', 'expenses', 'notes', 'rating']
        extra_kwargs = {
            'notes': {'write_only': True},
        }

class VisitDetailSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Visit
        fields = ['id', 'restaurant', 'visit_date', 'expenses', 'notes', 'rating']
