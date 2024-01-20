from rest_framework.permissions import BasePermission
from apps.Restaurant.models import Restaurant

class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'create':
            restaurant_id = request.data.get('restaurant')
            if restaurant_id:
                try:
                    restaurant = Restaurant.objects.get(pk=restaurant_id)
                    return request.user == restaurant.user
                except Restaurant.DoesNotExist:
                    return False
        return True


    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'DELETE']:
            return obj.user == request.user
        return request.user.is_authenticated