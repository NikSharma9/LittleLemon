from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from mixins import (
    UserMixin,
    MenuItemMixin,
)

class SetUpMixin:

    def setUp(self):
        self.user = self.create_user(
            username = 'test@email.com',
            password = 'testpasswd',
        )
        self.token = self.get_token(
            username = 'test@email.com',
            password = 'testpasswd',
        )
        self.client = Client(HTTP_AUTHORIZATION=f'JWT {self.token}')


class MenuItemViewTest(SetUpMixin, UserMixin, MenuItemMixin, TestCase):

    def setUp(self):
        self.create_menu_items()
        super().setUp()

    def test_list(self):
        response = self.client.get(reverse('api:menu'))
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        data = {'title': 'latte', 'price': 2.99, 'inventory': 5}
        response = self.client.post(reverse('api:menu'), data=data)
        serializer = MenuSerializer(Menu.objects.get(title='latte'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)