from django.contrib import admin
from .models import Event, Topic, Writeup


class TopicInline(admin.TabularInline):
    model = Topic
    fields = ("speaker", "title", "why", "what", "poster", "hook")


@admin.register(Event)
class EventAdminView(admin.ModelAdmin):
    model = Event
    list_display = ["episode", "datetime", "poster"]
    inlines = (TopicInline,)


@admin.register(Writeup)
class WriteupSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Writeup.objects.all().count()
        if count < 1:
            return True
        return False

    list_display = ("content",)
