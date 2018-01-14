from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import serializers
from api.models import Camera, Child, Event
from api.staticvars import KEY_LENGTH


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    email = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):
        return User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']))


class CameraSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=30)
    cameraid = serializers.CharField(required=True, max_length=30)
    userid = serializers.CharField(required=True, max_length=30)

    def create(self, validated_data):
        user = User.objects.filter(id=int(validated_data['userid']))
        key = get_random_string(length=KEY_LENGTH)

        return Camera.objects.create(
            name=validated_data['name'],
            cameraid=validated_date['cameraid'],
            key=key,
            user=user,)


class ChildSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)
    sex = serializers.CharField(required=True, max_length=1)

    def create(self, validated_data):
        user = User.objects.filter(id=int(self.context['userid'])).first()

        return Child.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            sex=validated_data['sex'],
            user=user,)
