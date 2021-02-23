from django.contrib import admin
from .models import Speaker


class SpeakerAdminView(admin.ModelAdmin):
    model = Speaker
    list_display = ["name", "position", "avatar"]


admin.site.register(Speaker, SpeakerAdminView)
