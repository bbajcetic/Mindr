import json
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.views.decorators.http import require_http_methods
from api.forms import (
    CameraRegisterForm,
    ChildRegisterForm,
    ParentRegisterForm,
)
from api.models import Camera, Child, Parent
from api.staticvars import KEY_LENGTH


@require_http_methods(["GET", "POST"])
def parents(request):
    """Registers a parent or sends back all parents."""
    if request.method == "POST":
        # Register a new parent
        form = ParentRegisterForm
        parent = form.save()
        parent.refresh_from_db()
        parent.save()

        # Return the parent just registered
        return json.load(parent)

    # Return all parents
    return json.load(Parent.objects.all())

@require_http_methods(["GET", "DELETE"])
def get_parent(request, parentid):
    """Sends back a parent or deletes a parent."""
    if request.method == "GET":
        # Send back a parent
        return json.load(Parent.objects.filter(id=parentid))

    # Delete the parent
    Parent.objects.filter(id=parentid)
    return HttpResponse(status=204)


@require_http_methods(["GET", "POST"])
def cameras(request, parentid):
    """Registers a camera or sends back all of a parent's cameras."""
    if request.method == "POST":
        # Register a new camera
        form = CameraRegisterForm()

        camera = form.save()
        camera.refresh_from_db()
        camera.key = get_random_string(length=KEY_LENGTH)
        camera.parent = request.user.parent
        camera.save()

        # Return the camera just registered
        return json.load(camera)

    # Return all of a parent's cameras
    return json.load(Camera.objects.filter(parent__id=parentid))

@require_http_methods(["GET", "DELETE"])
def get_camera(request, parentid, cameraid):
    """Sends back a camera or deletes a camera."""
    if request.method == "GET":
        # Send back the camera
        return json.load(Camera.objects.filter(id=cameraid))

    # Delete the camera
    Parent.objects.filter(id=cameraid)
    return HttpResponse(status=204)

@require_http_methods(["GET", "POST"])
def children(request, parentid):
    """Registers a child or sends back all of a parent's children."""
    if request.method == "POST":
        # Register a new child
        form = ChildRegisterForm()

        child = form.save()
        child.refresh_from_db()
        child.parent = request.user.parent
        child.save()

        # Return the child just registered
        return json.load(child)

    # Return all of a parent's children
    return json.load(Child.objects.filter(parent__id=parentid))

@require_http_methods(["GET", "DELETE"])
def get_child(request, parentid, childid):
    """Sends back a child or deletes a child."""
    if request.method == "GET":
        # Send back the child
        return json.load(Child.objects.filter(id=childid))

    # Delete the child
    Child.objects.filter(id=childid)
    return HttpResponse(status=204)

#@require_POST
#def register_event(request
