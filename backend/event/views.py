from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Event, Topic
from speaker.models import Speaker
from .serializers import EventCreateSerializer, EventReadSerializer, TopicReadSerializer


class EventView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer

    def create(self, request):
        data = request.data
        serializer = EventCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
        event = Event.objects.create(episode=data["episode"], datetime=data["datetime"])
        for topic in data["topic"]:
            speaker = Speaker.objects.get(pk=topic["speaker"])
            t = Topic.objects.create(
                speaker=speaker,
                event=event,
                title=topic["title"],
                why=topic["why"],
                what=topic["what"],
            )
        return Response(event.id)


class TopicView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicReadSerializer
