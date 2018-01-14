from rest_framework import serializers
from api.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    email = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']))
