from django.db import models
from speaker.models import Speaker


class Event(models.Model):
    episode = models.IntegerField()
    datetime = models.DateTimeField()
    poster = models.ImageField(upload_to="event_poster")


class EventSpeaker(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to="speaker_poster")
