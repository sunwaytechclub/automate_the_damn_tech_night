from functions.posters.speaker import generate_speaker_poster


def run():
    generate_speaker_poster(
        {
            "PROFILE PIC": "nick.jpg",
            "NAME": "Ding Nick Hong (Nick)",
            "POSITIONS": "STC President",
            "ACTIVITY": "Software Development Lifecycle",
            "WHY": "To enhance your workflow",
            "WHAT": "Overview of Software Development",
        }
    )
