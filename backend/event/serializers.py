from rest_framework import serializers
from .models import Event, Topic
from speaker.serializers import SpeakerSerializer
from functions.writeup.main import main as generate_writeup


class TopicReadSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ["id", "speaker", "title", "why", "what", "poster", "hook"]


class EventReadSerializer(serializers.ModelSerializer):
    topic = TopicReadSerializer(many=True)
    writeup = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "episode", "datetime", "writeup", "poster", "topic"]

    def get_writeup(self, obj):
        return generate_writeup(obj)


class TopicCreateSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ["speaker", "title", "why", "what", "hook"]


class EventCreateSerializer(serializers.ModelSerializer):
    topic = TopicCreateSerializer(many=True)

    class Meta:
        model = Event
        fields = ["episode", "datetime", "topic"]
