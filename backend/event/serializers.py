from rest_framework import serializers
from .models import Event, Topic
from speaker.serializers import SpeakerSerializer


class TopicSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ["speaker", "title", "why", "what"]


class EventSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=True)

    class Meta:
        model = Event
        fields = ["episode", "datetime", "topic"]
