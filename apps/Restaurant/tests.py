from django.test import TestCase
from django.contrib.auth.models import User
from .models import CuisineType, Restaurant

class RestaurantModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_str_representation(self):
        cuisine_type = CuisineType.objects.create(name='Italian')
        restaurant = Restaurant.objects.create(user=self.user, name='Test Restaurant', place='Test Place', cuisine_id=cuisine_type.pk)
        self.assertEqual(str(restaurant), 'Test Restaurant')

    def test_create_restaurant(self):
        cuisine_type = CuisineType.objects.create(name='Italian')
        restaurant = Restaurant.objects.create(user=self.user, name='Test Restaurant', place='Test Place', cuisine_id=cuisine_type.pk)
        self.assertEqual(Restaurant.objects.count(), 1)

    def test_update_restaurant(self):
        cuisine_type = CuisineType.objects.create(name='Italian')
        restaurant = Restaurant.objects.create(user=self.user, name='Old Name', place='Old Place', cuisine_id=cuisine_type.pk)
        restaurant.name = 'New Name'
        restaurant.place = 'New Place'
        restaurant.save()
        updated_restaurant = Restaurant.objects.get(id=restaurant.id)
        self.assertEqual(updated_restaurant.name, 'New Name')
        self.assertEqual(updated_restaurant.place, 'New Place')

    def test_delete_restaurant(self):
        cuisine_type = CuisineType.objects.create(name='Italian')
        restaurant = Restaurant.objects.create(user=self.user, name='ToDelete', place='ToDelete Place', cuisine_id=cuisine_type.pk)
        restaurant_id = restaurant.id
        restaurant.delete()
        with self.assertRaises(Restaurant.DoesNotExist):
            deleted_restaurant = Restaurant.objects.get(id=restaurant_id)