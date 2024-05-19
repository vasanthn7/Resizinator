from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


from image.models import Image
from image.serializers import ImageSerializer
from image.tasks import resize_image

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user.id)

    def create(self, request):
        if 'original' not in request.data:
            pass
        serializer = ImageSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            resize_image.delay(serializer.data['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
