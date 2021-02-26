from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Speaker
from .serializers import SpeakerSerializer


class SpeakerView(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer