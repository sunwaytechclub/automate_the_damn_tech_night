from django.contrib import admin
from .models import Event, EventSpeaker


class EventSpeakerInline(admin.TabularInline):
    model = EventSpeaker
    fields = ("speaker", "title", "why", "what")


@admin.register(Event)
class EventAdminView(admin.ModelAdmin):
    model = Event
    list_display = ["episode", "datetime"]
    inlines = (EventSpeakerInline,)
