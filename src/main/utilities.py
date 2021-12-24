import os
import math
from exif import Image as ExifImage
from exif import DATETIME_STR_FORMAT
from PIL import Image, ImageDraw, ImageFont, ExifTags
from django.conf import settings
from django.utils import timezone


def handle_uploaded_file(file):
    file_path = f'{ settings.MEDIA_ROOT }/{ file }'
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path


def edit_image(img_path, form_cd):
    img = Image.open(img_path)

    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    if img._getexif():
        exif = dict(img._getexif().items())
        try:
            if exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
        except BaseException:
            pass

    img_width, img_height = img.size

    datetime_str = form_cd['date'].strftime('%m/%d/%Y %H:%M:%S')
    gps_str = (
        f"{ form_cd['latitude_a'] }º "
        f"{ form_cd['latitude_m'] }' "
        f"{ form_cd['latitude_s'] }\" "
        f"{ form_cd['latitude_ref'] }, "
        f"{ form_cd['longitude_a'] }º "
        f"{ form_cd['longitude_m'] }' "
        f"{ form_cd['longitude_s'] }\" "
        f"{ form_cd['longitude_ref'] }"
    )

    dp = math.sqrt(math.pow(img_width, 2) + math.pow(img_height, 2))
    fnt_size = int(dp * 125 / 5040)
    datetime_width = int(img_width - (dp * 1280 / 5040))
    datetime_height = int(img_height - (dp * 380 / 5040))
    gps_height = int(img_height - (dp * 240 / 5040))

    if len(gps_str) == 28:
        gps_width = int(img_width - (dp * 1650 / 5040))
    elif len(gps_str) == 27:
        gps_width = int(img_width - (dp * 1580 / 5040))
    elif len(gps_str) == 26:
        gps_width = int(img_width - (dp * 1510 / 5040))
    elif len(gps_str) == 25:
        gps_width = int(img_width - (dp * 1440 / 5040))
    elif len(gps_str) == 24:
        gps_width = int(img_width - (dp * 1370 / 5040))
    elif len(gps_str) == 23:
        gps_width = int(img_width - (dp * 1300 / 5040))
    elif len(gps_str) == 22:
        gps_width = int(img_width - (dp * 1230 / 5040))
    else:
        gps_width = int(img_width - (dp * 1650 / 5040))

    fnt = ImageFont.truetype(
        f'{ settings.STATICFILES_DIRS[0] }/arialmt.ttf',
        fnt_size)
    d = ImageDraw.Draw(img)

    d.multiline_text((datetime_width, datetime_height), datetime_str,
                     font=fnt, fill=(255, 255, 255))
    d.multiline_text((gps_width, gps_height), gps_str,
                     font=fnt, fill=(255, 255, 255))

    pil_img_path = f'{ settings.MEDIA_ROOT }/{ timezone.now().timestamp() }.jpg'
    img.save(pil_img_path)

    with open(pil_img_path, 'rb') as pil_file:
        pil_image = ExifImage(pil_file)

        datetime_str = form_cd['date'].strftime(DATETIME_STR_FORMAT)
        pil_image.datetime = datetime_str
        pil_image.datetime_digitized = datetime_str
        pil_image.datetime_original = datetime_str

        gps_latitude = (
            form_cd['latitude_a'],
            form_cd['latitude_m'],
            form_cd['latitude_s'])
        gps_longitude = (
            form_cd['longitude_a'],
            form_cd['longitude_m'],
            form_cd['longitude_s'])
        pil_image.gps_latitude = gps_latitude
        pil_image.gps_latitude_ref = form_cd['latitude_ref']
        pil_image.gps_longitude = gps_longitude
        pil_image.gps_longitude_ref = form_cd['longitude_ref']

        datetime_str = form_cd['date'].strftime('%Y%m%d_%H%M%S')
        new_img_path = f"{ settings.MEDIA_ROOT }/IMG_{ datetime_str }.jpg"
        with open(new_img_path, 'wb') as new_image_file:
            new_image_file.write(pil_image.get_file())

    os.remove(pil_img_path)

    return new_img_path
