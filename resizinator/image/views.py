from rest_framework import viewsets
# from rest_framework.pagination import LimitOffsetPagination

from image.models import Image
from image.serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
