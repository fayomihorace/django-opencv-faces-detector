from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
	image = models.ImageField(upload_to="images")

class ImageName(models.Model):
	name = models.CharField(max_length=100, null=True,  unique=True)


@receiver(post_delete, sender=Image)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 