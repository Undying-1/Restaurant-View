from django.db import models
from django.contrib.auth.models import User
from apps.Restaurant.models import Restaurant


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    visit_date = models.DateField()
    expenses = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    
    def __str__(self):
        return self.restaurant.name