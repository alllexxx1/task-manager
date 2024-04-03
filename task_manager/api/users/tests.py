from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from task_manager.api.users.serializers import UserSerializer
from task_manager.users.tests import load_fixture


class UserAPITestCase(APITestCase):
    """
    Test case for the UserAPIView.

    This test case ensures that the API endpoint returns
    the expected list of users in the correct format.
    """

    fixtures = ['users.json']

    def test_get_users(self):
        """
        Test the retrieval of user data through the API.
        """
        url = reverse('user-list')
        response = self.client.get(url)
        users = get_user_model().objects.all()
        serialized_data = UserSerializer(users, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data, serialized_data)


class UserSerializerTestCase(TestCase):
    """
    Test case for the UserSerializer.

    This test case verifies the serialization process
    of the UserSerializer, ensuring that the serialized
    data matches the expected format.
    """

    fixtures = ['users.json']

    def test_serializer(self):
        """
        Verify that the UserSerializer correctly
        serializes user data into JSON format.
        """
        user = get_user_model().objects.get(id=1)
        serialized_data = UserSerializer(user).data
        expected_data = load_fixture('serialized_users.json')

        self.assertEqual(serialized_data, expected_data)
