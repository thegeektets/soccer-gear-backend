from rest_framework import serializers

from custom_auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'is_admin',
            'is_superuser'
        )

    is_admin = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    password = serializers.CharField(max_length=255, required=True)