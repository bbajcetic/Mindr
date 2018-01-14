from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework import serializers
import dateutil.parser
from api.models import Camera, Child, Emotion, Event
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


class EventSerializer(serializers.Serializer):
    childid = serializers.CharField(required=True, max_length=30)
    time = serializers.DateTimeField()
    significant = serializers.BooleanField()
    emotiondata = serializers.DictField(child=serializers.FloatField())

    def create(self, validated_data):
        child = Child.objects.filter(id=int(validated_data['childid']))
        emotion = Emotion.objects.create(
                    anger=validated_data['emotiondata:anger'],
                    disgusted=validated_data['emotiondata:disgusted'],
                    fearful=validated_data['emotiondata:fearful'],
                    happy=validated_data['emotiondata:happy'],
                    sad=validated_data['emotiondata:sad'],
                    surprised=validated_data['emotiondata:surprised'],
                    neutral=validated_data['emotiondata:neutral'],
                    )
        timeobject = dateutil.parser.parse(validated_data['time'])

        return Event.objects.create(
            time=timeobject,
            emotion=emotion,
            significant=validated_data['significant'],
            child=child,)
