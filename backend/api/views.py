from django.core import serializers
from django.utils.crypto import get_random_string
from django.views.decorators.http import require_http_methods
from api.forms import (
    CameraRegisterForm,
    ChildRegisterForm,
    ParentRegisterForm
)
from api.models import Camera, Child, Event, Parent
from api.staticvars import KEY_LENGTH
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import User
from api.serializers import UserSerializer


@csrf_exempt
@permission_classes((AllowAny, ))
@require_http_methods(["GET", "POST"])
def users(request):
    """Registers a parent or sends back all parents."""
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@permission_classes((AllowAny, ))
@require_http_methods(["GET", "POST"])
def parents(request):
    """Registers a parent or sends back all parents."""
    if request.method == "POST":
        # Register a new parent
        form = ParentRegisterForm(request.POST)
        parent = form.save()
        parent.refresh_from_db()
        parent.save()

        # Return the parent just registered
        response = serializers.serialize("json", parent)
        return HttpResponse(response, content_type='application/json')

    # Return all parents
    response = serializers.serialize("json", Parent.objects.all())
    return HttpResponse(response, content_type='application/json')


@require_http_methods(["GET", "DELETE"])
def get_parent(request, parentid):
    """Sends back a parent or deletes a parent."""
    if request.method == "GET":
        # Send back a parent
        response = serializers.serialize("json",
                                         Parent.objects.filter(id=parentid))
        return HttpResponse(response, content_type='application/json')

    # Delete the parent
    Parent.objects.filter(id=parentid).delete()
    return HttpResponse(status=204)


@require_http_methods(["GET", "POST"])
def cameras(request, parentid):
    """Registers a camera or sends back all of a parent's cameras."""
    if request.method == "POST":
        # Register a new camera
        form = CameraRegisterForm(request.POST)

        camera = form.save()
        camera.refresh_from_db()
        camera.key = get_random_string(length=KEY_LENGTH)
        camera.parent = request.user.parent
        camera.save()

        # Return the camera just registered
        response = serializers.serialize("json", camera)
        return HttpResponse(response, content_type='application/json')

    # Return all of a parent's cameras
    response = serializers.serialize("json",
                                Camera.objects.filter(parent__id=parentid))
    return HttpResponse(response, content_type='application/json')


@require_http_methods(["GET", "DELETE"])
def get_camera(request, parentid, cameraid):
    """Sends back a camera or deletes a camera."""
    if request.method == "GET":
        # Send back the camera
        response = serializers.serialize("json",
                                         Camera.objects.filter(id=cameraid))
        return HttpResponse(response, content_type='application/json')

    # Delete the camera
    Parent.objects.filter(id=cameraid).delete()
    return HttpResponse(status=204)


@require_http_methods(["GET", "POST"])
def children(request, parentid):
    """Registers a child or sends back all of a parent's children."""
    if request.method == "POST":
        # Register a new child
        form = ChildRegisterForm(request.POST)

        child = form.save()
        child.refresh_from_db()
        child.parent = request.user.parent
        child.save()

        # Return the child just registered
        response = serializers.serialize("json", child)
        return HttpResponse(response, content_type='application/json')

    # Return all of a parent's children
    response = serializers.serialize("json",
                                Child.objects.filter(parent__id=parentid))
    return HttpResponse(response, content_type='application/json')


@require_http_methods(["GET", "DELETE"])
def get_child(request, parentid, childid):
    """Sends back a child or deletes a child."""
    if request.method == "GET":
        # Send back the child
        response = serializers.serialize("json",
                                         Child.objects.filter(id=childid))
        return HttpResponse(response, content_type='application/json')

    # Delete the child
    Child.objects.filter(id=childid).delete()
    return HttpResponse(status=204)

@require_http_methods(["GET", "POST"])
def events(request, parentid, childid):
    """Registers an event or sends back all of a child's events."""
    if request.method == "POST":
        # Validate key
        valid_keys = (
            Camera.objects.filter(parent__id=parentid).values_list('key',
                                                                   flat=True))
        if request.POST['key'] not in valid_keys:
            # Not allowed!
            return HttpResponse(status=401)

        # Register an event - this is using the variables from the
        # temporary test model
        thechild = Child.objects.filter(id=childid)
        is_significant = request.POST['is_significant']
        happiness = request.POST['happiness']
        event = Event(child=thechild,
                      is_significant=is_significant,
                      happiness=happiness)
        event.save()

        # Return the event just registered
        response = serializers.serialize("json", event)
        return HttpResponse(response, content_type='application/json')

    # Return all of a child's events
    response = serializers.serialize("json",
                                Event.objects.filter(child__id=childid))
    return HttpResponse(response, content_type='application/json')

@require_http_methods(["GET", "DELETE"])
def get_event(request, parentid, childid, eventid):
    """Sends back an event or deletes an event."""
    if request.method == "GET":
        # Send back the event
        response = serializers.serialize("json",
                                         Event.objects.filter(id=eventid))
        return HttpResponse(response, content_type='application/json')

    # Delete the event
    Event.objects.filter(id=eventid).delete()
    return HttpResponse(status=204)
