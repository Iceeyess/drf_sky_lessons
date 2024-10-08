from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from requests.auth import HTTPBasicAuth
from rest_framework_simplejwt.tokens import Token
from django.urls import reverse, reverse_lazy
import json
from users.models import User
from vehicle.models import Moto, Car


# Create your tests here.


class VehicleTestCase(APITestCase):
    """Тестирование модели Vehicle"""

    def setUp(self) -> None:
        # user creation
        self.user_date = dict(username='iceeyes', password='1234', email='test@gmail.com')
        self.client = APIClient()
        self.user = User.objects.create_user(**self.user_date)
        #   auth user
        self.auth_url = reverse('token_obtain_pair')
        self.access_token = self.client.post(self.auth_url, {
            'username': self.user_date.get('username'),
            'password': self.user_date.get('password')
        }).data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def test_create_moto(self):
        """Тестирование создание Мото"""
        data = {
            'title': 'Test moto',
            'description': 'Test moto description',
            'milage': []
        }
        moto_url = reverse_lazy('vehicle:moto-create')
        response = self.client.post(path=moto_url, format='json', data=data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content).get('title'), 'Test moto')
        data |= {'id': 1}  # Для тестирования содержимого модели
        self.assertEqual(response.json(), data)
        self.assertTrue(Moto.objects.all().exists())

    def test_list_moto(self):
        """Тестирование списка мото"""
        Moto.objects.create(title='Test moto', description='Test description')
        url = reverse('vehicle:moto-list')
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json().get('results')) > 0)

    def test_create_car(self):
        """Тестирование создание машин"""
        data = {
            'title': 'Test car',
            'description': 'Test car description',
            'milage': [],
        }
        car_url = reverse_lazy('vehicle:car-list')
        response = self.client.post(path=car_url, format='json', data=data, headers=self.headers)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content).get('title'), 'Test car')
        data |= {'id': 1}  # Для тестирования содержимого модели
        self.assertEqual(response.json(), data)
        self.assertTrue(Car.objects.all().exists())