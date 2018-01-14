from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from api.models import Camera, Child, Event
from api.serializers import (
        UserSerializer,
        CameraSerializer,
        ChildSerializer,
)


@csrf_exempt
@permission_classes((AllowAny, ))
@require_http_methods(["GET", "POST"])
def users(request):
    """Registers a user or sends back all users."""
    if request.method == "POST":
        # Register a new user
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            # Return the user just registered
            return JsonResponse(serializer.data, status=201)

        # Invalid data
        return JsonResponse(serializer.errors, status=400)

    # Return all users
    response = serializers.serialize("json", Parent.objects.all())
    return HttpResponse(response, status=200)


@require_http_methods(["GET", "DELETE"])
def get_user(request, userid):
    """Sends back a user or deletes a user."""
    if request.method == "GET":
        # Send back a user
        response = serializers.serialize(
                                    "json",
                                    [User.objects.filter(id=userid).first()])
        return HttpResponse(response, status=200)

    # Delete the user
    User.objects.filter(id=userid).delete()
    return JsonResponse(status=204)


@require_http_methods(["GET", "POST"])
def cameras(request, userid):
    """Registers a camera or sends back all of a user's cameras."""
    if request.method == "POST":
        # Register a new camera
        data = JSONParser().parse(request)
        serializer = CameraSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            # Return the camera just registered
            return JsonResponse(serializer.data, status=201)

        # Invalid data
        return JsonResponse(serializer.errors, status=400)

    # Return all of a user's cameras
    response = serializers.serialize("json",
                                Camera.objects.filter(parent__id=parentid))
    return HttpResponse(response, status=200)


@require_http_methods(["GET", "DELETE"])
def get_camera(request, userid, cameraid):
    """Sends back a camera or deletes a camera."""
    if request.method == "GET":
        # Send back the camera
        response = serializers.serialize("json",
                                 [Camera.objects.filter(id=cameraid).first()])
        return HttpResponse(response, status=200)

    # Delete the camera
    Camera.objects.filter(id=cameraid).delete()
    return JsonResponse(status=204)


@require_http_methods(["GET", "POST"])
def children(request, userid):
    """Registers a child or sends back all of a user's children."""
    if request.method == "POST":
        # Register a new child
        data = JSONParser().parse(request)
        serializer = ChildSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            # Return the child just registered
            return JsonResponse(serializer.data, status=201)

        # Invalid data
        return JsonResponse(serializer.errors, status=400)

    # Return all of a user's children
    response = serializers.serialize("json",
                                Child.objects.filter(user__id=userid))
    return HttpResponse(response, status=200)


@require_http_methods(["GET", "DELETE"])
def get_child(request, userid, childid):
    """Sends back a child or deletes a child."""
    if request.method == "GET":
        # Send back the child
        response = serializers.serialize("json",
<<<<<<< Updated upstream
                                    [Child.objects.filter(id=childid).first()])
        return HttpResponse(response, status=200)
=======
                                         [Child.objects.filter(id=childid).first()])
        return JsonResponse(response, status=200)
>>>>>>> Stashed changes

    # Delete the child
    Child.objects.filter(id=childid).delete()
    return JsonResponse(status=204)


@require_http_methods(["GET", "POST"])
def events(request, userid, childid):
    """Registers an event or sends back all of a child's events."""
    if request.method == "POST":
        # Validate key
        valid_keys = (
            Camera.objects.filter(user__id=userid).values_list('key',
                                                               flat=True))
        if request.POST['key'] not in valid_keys:
            # Not allowed!
            return JsonResponse(status=401)

        # Register an event
        thechild = Child.objects.filter(id=childid)
        event = Event(child=thechild,
                      data=request.POST['data'])

        # Return the event just registered
        response = serializers.serialize("json", event)
        return JsonResponse(response, status=201)

    # Return all of a child's events
    response = serializers.serialize("json",
                                Event.objects.filter(child__id=childid))
    return HttpResponse(response, status=200)



@require_http_methods(["GET", "DELETE"])
def get_event(request, parentid, childid, eventid):
    """Sends back an event or deletes an event."""
    if request.method == "GET":
        # Send back the event
        response = serializers.serialize("json",
                                   [Event.objects.filter(id=eventid).first()])
        return HttpResponse(response, status=200)

    # Delete the event
    Event.objects.filter(id=eventid).delete()
    return JsonResponse(status=204)
