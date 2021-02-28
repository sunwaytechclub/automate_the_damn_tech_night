from event.models import Writeup, Speaker, Event
from event.serializers import EventReadSerializer
import re


def run():
    event = Event.objects.first()
    event_serializer = EventReadSerializer(instance=event).data

    writeup = Writeup.objects.first()
    content = writeup.content
    res = re.finditer("{{ .{1,10} }}", content)
    switch = {
        "hooks": hooks,
        "topics": topics,
        "episode": episode,
        "datetime": datetime,
    }
    for result in res:
        # span = [result.start, result.end]
        param = result.group().strip("{{ ").strip(" }}")
        value = switch[param](event_serializer, event)
        content = content.replace(result.group(), str(value))
    print(content)


def hooks(data, event):
    hook = ""
    for topic in data["topic"]:
        hook += f'"{topic["hook"]}"' + "\n"
    return hook


def topics(data, event):
    topic = ""
    for t in data["topic"]:
        topic += t["title"] + "!" + "\n"
    return topic


def episode(data, event):
    return event.episode


def datetime(data, event):
    return event.datetime.strftime("%d.%m.%Y %I:%M %p")
