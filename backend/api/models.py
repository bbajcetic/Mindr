from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    user= models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            null=True)


class Child(models.Model):
    """A child."""
    # Basic child info
    first_name = models.CharField(max_length=30,
                                  verbose_name="first name")
    last_name = models.CharField(max_length=30,
                                  verbose_name="last name")
    sex = models.CharField(max_length=1,
                           choices=(('F', 'F'),
                                    ('M', 'M'),
                                    ('X', 'X'),),
                           default='F',)

    # The user "owning" the child
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True)

    def __str__(self):
        """String representation of a child."""
        return "%s %s" % (self.first_name, self.last_name)


class Event(models.Model):
    """Data from a screen capture."""
    # The child in the screen capture
    child = models.ForeignKey(Child,
                              on_delete=models.CASCADE,
                              null=True)

    # JSON emotion data
    data = JSONField()
