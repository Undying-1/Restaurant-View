from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Visit
from .serializers import VisitListSerializer, VisitDetailSerializer
from apps.Users.permissions import IsOwnerOrReadOnly
from apps.Restaurant.models import Restaurant

class VisitListView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitListSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['id', 'rating',]
    search_fields = ['restaurant__name', 'visit_date', 'rating']
    filterset_fields = ['id','restaurant__name', 'rating',]


    def perform_create(self, serializer):
        restaurant_id = self.request.data.get('restaurant')
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
            if restaurant.user == self.request.user:
                serializer.save(user=self.request.user, restaurant=restaurant)
            else:
                self.permission_denied(self.request, message="You are not the owner of this restaurant.")
        except Restaurant.DoesNotExist:
            self.permission_denied(self.request, message="Restaurant does not exist.")
        
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs).data
        queryset = Visit.objects.values('visit_date').annotate(expenses=Avg('expenses', default=0), rating=Avg('rating', default=0)).order_by()
        serializer_class = VisitListSerializer(queryset, many=True)
        response['results'] = serializer_class.data
        return Response(response)
    
    
    def destroy(self, request, *args, **kwargs):
            username = request.user.username
            user = get_object_or_404(User, username=username)
            try:
                visits = Visit.objects.filter(user=user).all()
                visits.delete()
            except Exception as e:
                return JsonResponse(status=409, data={'message':"Error while deleting Visits"})
            return JsonResponse(status=200, data={'message':"Visits deleted"})
        

class VisitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]