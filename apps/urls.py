from django.urls import path, include


urlpatterns = [
    path('restaurants/', include('apps.Restaurant.urls')),
    path('visits/', include('apps.Visit.urls')),
]