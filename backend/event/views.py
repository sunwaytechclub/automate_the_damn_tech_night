from django.core.files.images import ImageFile
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from speaker.models import Speaker
from .models import Event, Topic
from .serializers import (
    EventCreateSerializer,
    EventReadSerializer,
    TopicReadSerializer,
)
from functions.posters.event import generate_event_poster
from functions.posters.speaker import generate_speaker_poster


class EventView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer

    def partial_update(self, request, pk=None):
        serializer = EventCreateSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        event = Event.objects.get(pk=pk)

        event.episode = data.get("episode", event.episode)
        event.datetime = data.get("datetime", event.datetime)

        if data.get("topic"):
            # Delete all topic
            Topic.objects.filter(event=event).delete()
            for topic in request.data["topic"]:
                speaker = Speaker.objects.get(pk=topic["speaker"])
                # Re-generate speaker poster
                poster = ImageFile(
                    generate_speaker_poster(
                        {
                            "PROFILE PIC": speaker.avatar.name.split("/")[-1],
                            "NAME": speaker.name,
                            "POSITIONS": speaker.position,
                            "ACTIVITY": topic["title"],
                            "WHY": topic["why"],
                            "WHAT": topic["what"],
                        }
                    ),
                    name=f"{event.episode}-{speaker.name}.jpg",
                )
                t = Topic.objects.create(
                    speaker=speaker,
                    event=event,
                    hook=topic['hook']
                    title=topic["title"],
                    why=topic["why"],
                    what=topic["what"],
                    poster=poster,
                )
        # Re-generate event poster
        poster = ImageFile(
            generate_event_poster(
                event.episode,
                # Date
                event.datetime.strftime("%d.%m.%Y"),
                # Time
                event.datetime.strftime("%I:%M %p"),
            ),
            name=f"{event.episode}.jpg",
        )
        event.poster = poster
        event.save()
        return Response(EventReadSerializer(instance=event).data)

    def create(self, request):
        data = request.data
        serializer = EventCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        datetime = serializer.validated_data["datetime"]
        poster = ImageFile(
            generate_event_poster(
                data["episode"],
                # Date
                datetime.strftime("%d.%m.%Y"),
                # Time
                datetime.strftime("%I:%M %p"),
            ),
            name=f"{data['episode']}.jpg",
        )
        event = Event.objects.create(
            episode=data["episode"],
            datetime=data["datetime"],
            poster=poster,
        )
        for topic in data["topic"]:
            speaker = Speaker.objects.get(pk=topic["speaker"])
            poster = ImageFile(
                generate_speaker_poster(
                    {
                        "PROFILE PIC": speaker.avatar.name.split("/")[-1],
                        "NAME": speaker.name,
                        "POSITIONS": speaker.position,
                        "ACTIVITY": topic["title"],
                        "WHY": topic["why"],
                        "WHAT": topic["what"],
                    }
                ),
                name=f"{data['episode']}-{speaker.name}.jpg",
            )
            t = Topic.objects.create(
                speaker=speaker,
                event=event,
                hook=topic["hook"],
                title=topic["title"],
                why=topic["why"],
                what=topic["what"],
                poster=poster,
            )
        return Response(EventReadSerializer(instance=event).data)


class TopicView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicReadSerializer
