from django.db import models

# Create your models here.
class Image(models.Model):
    original = models.ImageField(upload_to='images/')
    small = models.ImageField(upload_to='images/', blank=True, null=True)
    medium = models.ImageField(upload_to='images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.original.delete()
        self.small.delete()
        self.medium.delete()
        super().delete(*args, **kwargs)
