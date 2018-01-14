from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from datetime import timedelta
from api.models import Camera, Event
from api.serializers import (
        UserSerializer,
        CameraSerializer,
        EventSerializer,
)

EMPTY_JSON_SET = serializers.serialize("json", set())


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
    response = serializers.serialize("json", User.objects.all())
    return HttpResponse(response, status=200)


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def get_user(request, userid):
    """Sends back a user or deletes a user."""
    # Load the user
    user = User.objects.filter(id=userid)

    if not user:
        # Return empty set
        return HttpResponse(EMPTY_JSON_SET, status=200)

    if request.method == "GET":
        # Send back a user
        response = serializers.serialize("json", [user.first()])
        return HttpResponse(response, status=200)

    # Delete the user
    User.objects.filter(id=userid).first().delete()
    return JsonResponse(status=204)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def cameras(request, userid):
    """Registers a camera or sends back all of a user's cameras."""
    if request.method == "POST":
        # Register a new camera
        data = JSONParser().parse(request)
        serializer = CameraSerializer(data=data, context={'userid': userid})

        if serializer.is_valid():
            serializer.save()

            # Return the camera just registered
            return JsonResponse(serializer.data, status=201)

        # Invalid data
        return JsonResponse(serializer.errors, status=400)

    # Return all of a user's cameras
    response = serializers.serialize("json",
                                Camera.objects.filter(user__id=userid))
    return HttpResponse(response, status=200)


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def get_camera(request, userid, cameraid):
    """Sends back a camera or deletes a camera."""
    # Load the camera
    camera = Camera.objects.filter(id=cameraid)

    if not camera:
        # Return empty set
        return HttpResponse(EMPTY_JSON_SET, status=200)

    if request.method == "GET":
        # Send back the camera
        response = serializers.serialize("json", [camera.first()])
        return HttpResponse(response, status=200)

    # Delete the camera
    Camera.objects.filter(id=cameraid).first().delete()
    return HttpResponse(EMPTY_JSON_SET, status=204)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def events(request, userid, cameraid):
    """Registers an event or sends back all of a camera's events."""
    if request.method == "POST":
        # Get valid keys
        valid_keys = (
            Camera.objects.filter(user__id=userid).values_list('key',
                                                               flat=True))
        # Parse request as JSON
        data = JSONParser().parse(request)

        # Validate key
        if data["key"] not in valid_keys:
            # Not allowed!
            return JsonResponse(status=401)

        # Register an event
        serializer = EventSerializer(data=data, context={'cameraid': cameraid})

        if serializer.is_valid():
            serializer.save()

            # Return the event just registered
            return JsonResponse(serializer.data, status=201)

        # Invalid data
        return JsonResponse(serializer.errors, status=400)

    # Return all of a camera's events
    response = serializers.serialize("json",
                                Event.objects.filter(camera__id=cameraid))
    return HttpResponse(response, status=200)


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def get_event(request, userid, cameraid, eventid):
    """Sends back an event or deletes an event."""
    # Load the event
    event = Event.objects.filter(id=eventid)

    if not event:
        # Return empty set
        return HttpResponse(EMPTY_JSON_SET, status=200)

    if request.method == "GET":
        # Send back the event
        response = serializers.serialize("json", [event.first()])
        return HttpResponse(response, status=200)

    # Delete the event
    Event.objects.filter(id=eventid).first().delete()
    return HttpResponse(EMPTY_JSON_SET, status=204)


@require_http_methods(["GET"])
def get_significant_events(request, userid):
    user = User.objects.filter(id=userid).first()
    significant_events = (
        Event.objects.filter(
                        camera__user__id=userid).filter(
                        significant=True).filter(
                        time__gt=F('time') + timedelta(hours=-24)).order_by(
                        '-time')
        )

    response = serializers.serialize("json", significant_events)
    return HttpResponse(response, status=200)


@require_http_methods(["GET"])
def get_emotion_average(request, userid, cameraid, numevents):
    events = Event.objects.filter(camera__id=cameraid).order_by('-id')[:numevents]
    averages = {"angry": 0,
                "disgusted": 0,
                "fearful": 0,
                "happy": 0,
                "sad": 0,
                "surprised": 0,
                "neutral": 0}

    # Compute averages
    for event in events:
        for key in averages.keys():
            averages[key] += float(event.emotion[key])

    for key in averages.keys():
        averages[key] /= numevents

    return JsonResponse(averages, status=200)
