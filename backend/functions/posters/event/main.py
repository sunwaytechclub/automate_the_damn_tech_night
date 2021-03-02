from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
from django.conf import settings
import os
import io

TEXT_Y_PIXEL = 680
TEXT_SIZE = 36
TEMPLATE_IMG = os.path.join(settings.BASE_DIR, "./functions/posters/event/poster.png")
FONT_TTF_FILE = os.path.join(
    settings.BASE_DIR, "./functions/posters/event/Montserrat-Medium.otf"
)


def generate_event_poster(episode_number, date, time):
    formatted_event_detail = (
        "EPISODE " + str(episode_number) + "   " + str(date) + "  " + str(time)
    )
    img = Image.open(TEMPLATE_IMG)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(FONT_TTF_FILE, TEXT_SIZE)
    # draw.text((x, y),"Sample Text",(r,g,b))
    img_width, _ = img.size
    text_width, _ = font.getsize(formatted_event_detail.upper())

    draw.text(
        (img_width / 2 - text_width / 2, TEXT_Y_PIXEL),
        formatted_event_detail.upper(),
        (255, 255, 255),
        font=font,
    )
    # Save in memory not on disk
    output = io.BytesIO()
    img.save(output, format="JPEG")
    output.seek(0)

    return output


if __name__ == "__main__":
    generate_event_poster(1, "13.01.2020", "6.00PM")
