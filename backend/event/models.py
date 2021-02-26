from django.db import models
from speaker.models import Speaker


class Event(models.Model):
    episode = models.IntegerField(unique=True)
    datetime = models.DateTimeField()


class Topic(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name="topic")
    speaker = models.ForeignKey(
        to=Speaker, on_delete=models.CASCADE, related_name="topic"
    )
    title = models.CharField(max_length=58)
    why = models.CharField(max_length=58)
    what = models.CharField(max_length=58)
