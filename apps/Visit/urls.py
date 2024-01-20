from django.urls import path
from .views import VisitListView, VisitDetailView



urlpatterns = [
    path('', VisitListView.as_view(), name='visit-list'),
    path('<int:pk>/', VisitDetailView.as_view(), name='visit-detail'),
]
