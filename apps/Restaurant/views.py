from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer
from apps.Users.permissions import IsOwnerOrReadOnly



class RestaurantListView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'name',]
    search_fields = ['name', 'place', 'cuisine__name']
    filterset_fields = ['id','name', 'place',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, cuisine_id=self.request.data.get('cuisine_id'))
        
    def destroy(self, request, *args, **kwargs):
            username = request.user.username
            user = get_object_or_404(User, username=username)
            try:
                restaurants = Restaurant.objects.filter(user=user).all()
                restaurants.delete()
            except Exception as e:
                return JsonResponse(status=409, data={'message':"Error while deleting Restaurants"})
            return JsonResponse(status=200, data={'message':"Restaurants deleted"})

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    
    def perform_update(self, serializer):
        serializer.validated_data['cuisine_id'] = self.request.data.get('cuisine_id')
        serializer.save()