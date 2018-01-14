from django.contrib import admin
from api.models import Camera, Event

class CameraAdmin(admin.ModelAdmin):
    """Interface modifiers for the Camera model for the admin page."""
    list_display = ('name', 'cameraid', 'key', 'user')

class EventAdmin(admin.ModelAdmin):
    """Interface modifiers for the Camera model for the admin page."""
    list_display = ('camera', 'time', 'significant')

admin.site.register(Camera, CameraAdmin)
admin.site.register(Event)
