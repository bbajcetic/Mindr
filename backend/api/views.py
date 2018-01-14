import json
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.utils.crypto import get_random_string
from api.models import Camera


@require_POST
def register_camera(request, parentid):
    """Registers a camera."""
    form = CameraRegisterForm()

    camera = form.save()
    camera.refresh_from_db()
    camera.key = get_random_string(length=KEY_LENGTH)
    camera.parent = request.user.parent
    camera.save()

    return json.load(camera)
