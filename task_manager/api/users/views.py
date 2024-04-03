from rest_framework import generics
from django.contrib.auth import get_user_model
from task_manager.api.users.serializers import UserSerializer


class UserAPIView(generics.ListAPIView):
    """
    API view for retrieving a list of users.

    This view extends the generics.ListAPIView class
    provided by Django Rest Framework (DRF).
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
