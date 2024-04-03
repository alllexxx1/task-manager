from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from task_manager.api.users.serializers import UserSerializer
from task_manager.users.tests import load_fixture


class UserAPITestCase(APITestCase):
    fixtures = ['users.json']

    def test_get_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        users = get_user_model().objects.all()
        serialized_data = UserSerializer(users, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data, serialized_data)


class UserSerializerTestCase(TestCase):
    fixtures = ['users.json']

    def test_serializer(self):
        user = get_user_model().objects.get(id=1)
        serialized_data = UserSerializer(user).data
        expected_data = load_fixture('serialized_users.json')

        self.assertEqual(serialized_data, expected_data)
