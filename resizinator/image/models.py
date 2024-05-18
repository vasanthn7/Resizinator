from django.db import models

# Create your models here.
class Image(models.Model):
    original = models.ImageField(upload_to='')
    small = models.ImageField(upload_to='', blank=True, null=True)
    medium = models.ImageField(upload_to='', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.original.delete()
        self.small.delete()
        self.medium.delete()
        return super().delete(*args, **kwargs)
