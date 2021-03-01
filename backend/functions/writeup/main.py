from event.models import Writeup, Speaker, Event

import dateutil.parser
import re


def main(event):
    try:
        from event.serializers import EventCreateSerializer
    except ImportError:
        pass
    event_serializer = EventCreateSerializer(instance=event).data

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
    return content


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
    dt = dateutil.parser.isoparse(data["datetime"])
    return dt.strftime("%d.%m.%Y %I:%M %p")
