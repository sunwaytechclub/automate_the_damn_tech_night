from django.contrib import admin
from .models import Event, Topic


class TopicInline(admin.TabularInline):
    model = Topic
    fields = ("speaker", "title", "why", "what", "poster")


@admin.register(Event)
class EventAdminView(admin.ModelAdmin):
    model = Event
    list_display = ["episode", "datetime", "poster"]
    inlines = (TopicInline,)
