from rest_framework import serializers

from image.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ['small', 'medium', 'updated_at', 'created_at', 'user']

    def validate(self, attrs):
        attrs['user'] = self.context['user']
        validated_data = super().validate(attrs)
        return validated_data
