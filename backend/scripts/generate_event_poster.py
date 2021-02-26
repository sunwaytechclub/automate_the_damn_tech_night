from functions.posters.event import generate_event_poster


def run():
    img = generate_event_poster(1, "01.13.2020", "6.00PM")
    print(img)
