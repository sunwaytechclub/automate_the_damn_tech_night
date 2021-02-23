from functions.posters.speaker import generate_speaker_poster
from speaker.models import Speaker
from django.conf import settings


def run():
    speaker = Speaker.objects.first()
    file_name = speaker.avatar.name.split("/")[-1]
    generate_speaker_poster(
        {
            "PROFILE PIC": file_name,
            "NAME": speaker.name,
            "POSITIONS": speaker.position,
            "ACTIVITY": "ABCD ABCD ABCD ABCD ABCD ABCD\nABCD ABCD ABCD ABCD ABCD ABCD",
            "WHY": "To enhance your workflow",
            "WHAT": "Overview of Software Development",
        }
    )
