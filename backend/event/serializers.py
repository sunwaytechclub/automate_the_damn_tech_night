from rest_framework import serializers
from .models import Event, Topic
from speaker.serializers import SpeakerSerializer


class TopicReadSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ["id", "speaker", "title", "why", "what"]


class EventReadSerializer(serializers.ModelSerializer):
    topic = TopicReadSerializer(many=True)

    class Meta:
        model = Event
        fields = ["id", "episode", "datetime", "topic"]


class TopicCreateSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ["speaker", "title", "why", "what"]


class EventCreateSerializer(serializers.ModelSerializer):
    topic = TopicCreateSerializer(many=True)

    class Meta:
        model = Event
        fields = ["episode", "datetime", "topic"]
