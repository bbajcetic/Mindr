from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from api.models import Camera

class CameraRegisterForm(forms.ModelForm):
    """A form to register a new camera."""
    class Meta:
        model = Camera
        fields = ('name',)

class ParentRegisterForm(UserCreationForm):
    """A form to register a new parent."""
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
