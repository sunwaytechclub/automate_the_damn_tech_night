from django.db import models
from speaker.models import Speaker


class Event(models.Model):
    episode = models.IntegerField()
    datetime = models.DateTimeField()


class EventSpeaker(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    speaker = models.ForeignKey(to=Speaker, on_delete=models.CASCADE)
