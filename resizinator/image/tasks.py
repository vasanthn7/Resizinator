from io import BytesIO
from PIL import Image as Img

from celery import shared_task
from django.core.files.storage import default_storage

from image.models import Image

SMALL_HEIGHT = 100
MEDIUM_HEIGHT = 300

@shared_task
def resize_image(image_id):
    image = Image.objects.get(id=image_id)
    with default_storage.open(image.original.name, 'rb') as f:
        image_data = BytesIO(f.read())
    original = Img.open(image_data)

    small = original.resize((round(original.width/(original.height/SMALL_HEIGHT)), SMALL_HEIGHT))
    small_io = BytesIO()
    small.save(small_io, format=original.format)
    with default_storage.open(f'small_{image.original.name}', 'wb') as f:
        f.write(small_io.getvalue())
    image.small.save(f'small_{image.original.name}', small_io)

    medium = original.resize((round(original.width/(original.height/MEDIUM_HEIGHT)), MEDIUM_HEIGHT))
    medium_io = BytesIO()
    medium.save(medium_io, format=original.format)
    with default_storage.open(f'medium_{image.original.name}', 'wb') as f:
        f.write(medium_io.getvalue())
    image.medium.save(f'medium_{image.original.name}', medium_io)
    image.save()

    image_data.close()
