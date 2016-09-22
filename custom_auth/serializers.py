from rest_framework import serializers

from custom_auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
