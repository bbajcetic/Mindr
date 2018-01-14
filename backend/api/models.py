from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.staticvars import KEY_LENGTH


class Parent(models.Model):
    """A parent."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of a parent."""
        return "%s" % self.user.username


class Camera(models.Model):
    """A device which sends information to the server.

    Each device has a key which is verified before it can post data to
    the server
    """
    name = models.CharField(max_length=30,
                            verbose_name="camera name")
    key = models.CharField(max_length=KEY_LENGTH)
    parent = models.ForeignKey(Parent,
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

    # The parent "owning" the child
    parent = models.ForeignKey(Parent,
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

    # Emotion data - the below are used for testing right now, i.e.
    # they're not final
    is_significant = models.BooleanField()
    happiness = models.IntegerField()

@receiver(post_save, sender=User)
def update_user_parent(sender, instance, created, **kwargs):
    """Updates a user's 'parent'."""
    if created:
        Parent.objects.create(user=instance)
    instance.parent.save()
