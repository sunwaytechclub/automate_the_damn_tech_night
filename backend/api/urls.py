from django.urls import path, include
from rest_framework import routers
from event.views import EventView, TopicView
from speaker.views import SpeakerView

router = routers.SimpleRouter()
router.register("event", EventView)
router.register("speaker", SpeakerView)

urlpatterns = router.urls