from restaurant.models import Menu
from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="MenuItem1", price=11, menu_item_description="MenuItem1...")
        Menu.objects.create(name="MenuItem2", price=9, menu_item_description="MenuItem2...")

    def test_getall(self):
        response = self.client.get('/api/menu/')
        data = response.json()
        self.assertEqual(data['count'], 3)
