from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from api.staticvars import KEY_LENGTH


class Camera(models.Model):
    """A device which sends information to the server.

    Each device has a key which is verified before it can post data to
    the server
    """
    name = models.CharField(max_length=30,
                            verbose_name="camera name")
    cameraid = models.CharField(max_length=100)
    key = models.CharField(max_length=KEY_LENGTH)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True)


class Event(models.Model):
    """Data from a screen capture."""
    camera = models.ForeignKey(Camera,
                              on_delete=models.CASCADE,
                              null=True)
    time = models.DateTimeField(default=timezone.now)
    significant = models.BooleanField(default=False)
    emotion = JSONField()
