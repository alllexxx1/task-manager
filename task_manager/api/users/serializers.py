from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing User data.

    This serializer converts User model instances into
    JSON format and specifies the fields to include.
    """

    class Meta:
        """This class specifies metadata options for the serializer."""
        model = get_user_model()
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'is_superuser',
            'is_staff'
        )
