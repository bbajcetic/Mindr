import json
from django import forms
from api.models import Camera, Parent

class CameraRegisterForm(form.ModelForm):
    """A form to register a new camera."""
    class Meta:
        model = Camera
        fields = ('name')
