from django.test import TestCase
from django.contrib.auth.models import User
from .models import  Visit
from apps.Restaurant.models import CuisineType, Restaurant

class VisitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.cuisine_type = CuisineType.objects.create(name='Italian')
        self.restaurant = Restaurant.objects.create(user=self.user, name='Test Restaurant', place='Test Place', cuisine=self.cuisine_type)

    def test_str_representation(self):
        visit = Visit.objects.create(user=self.user, restaurant=self.restaurant, visit_date='2024-01-01', expenses='50.00', notes='Test Visit', rating=4)
        expected_str = f'{visit.visit_date}'
        self.assertEqual(str(visit.visit_date), expected_str)

    def test_create_visit(self):
        visit = Visit.objects.create(user=self.user, restaurant=self.restaurant, visit_date='2024-01-01', expenses='50.00', notes='Test Visit', rating=4)
        self.assertEqual(Visit.objects.count(), 1)

    def test_update_visit(self):
        visit = Visit.objects.create(user=self.user, restaurant=self.restaurant, visit_date='2024-01-01', expenses='50.00', notes='Test Visit', rating=4)
        visit.expenses = '75.00'
        visit.save()
        updated_visit = Visit.objects.get(id=visit.id)
        self.assertEqual(str(updated_visit.expenses), '75.00')

    def test_delete_visit(self):
        visit = Visit.objects.create(user=self.user, restaurant=self.restaurant, visit_date='2024-01-01', expenses='50.00', notes='Test Visit', rating=4)
        visit_id = visit.id
        visit.delete()
        with self.assertRaises(Visit.DoesNotExist):
            deleted_visit = Visit.objects.get(id=visit_id)