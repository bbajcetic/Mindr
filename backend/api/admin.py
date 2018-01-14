from django.contrib import admin
from api.models import Camera, Child, Event, Parent

class ParentAdmin(admin.ModelAdmin):
    """Interface modifiers for the Profile model for the admin page."""
    list_display = ('__str__')

admin.site.register(Camera)
admin.site.register(Child)
admin.site.register(Event)
admin.site.register(Parent)
