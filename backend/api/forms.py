from django import forms
from api.models import Camera

class CameraRegisterForm(forms.ModelForm):
    """A form to register a new camera."""
    class Meta:
        model = Camera
        fields = ('name',)
