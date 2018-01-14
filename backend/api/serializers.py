from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import serializers
from api.models import Camera, Event
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

    def create(self, validated_data):
        user = User.objects.filter(id=int(self.context['userid'])).first()
        key = get_random_string(length=KEY_LENGTH)

        return Camera.objects.create(
            name=validated_data['name'],
            cameraid=validated_date['cameraid'],
            key=key,
            user=user,)


class EventSerializer(serializers.Serializer):
    time = serializers.DateTimeField()
    significant = serializers.BooleanField()
    emotion = serializers.JSONField()

    def create(self, validated_data):
        camera = Camera.objects.filter(id=int(self.context['cameraid'])).first()
        emotiondict = validated_data['emotion']
        timeobject = validated_data['time']

        # Create the event
        return Event.objects.create(
            time=timeobject,
            significant=validated_data['significant'],
            emotion=validated_data['emotion'],
            camera=camera,)
