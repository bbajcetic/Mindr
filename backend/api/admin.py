from django.contrib import admin
from api.models import Camera, Child, Event

class CameraAdmin(admin.ModelAdmin):
    """Interface modifiers for the Camera model for the admin page."""
    list_display = ('name', 'cameraid', 'key', 'user')

class ChildAdmin(admin.ModelAdmin):
    """Interface modifiers for the Camera model for the admin page."""
    list_display = ('first_name', 'last_name', 'sex', 'user')

admin.site.register(Camera, CameraAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Event)
