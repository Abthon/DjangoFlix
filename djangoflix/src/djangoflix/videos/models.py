from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField()
    description = models.TextField()
    slug = models.SlugField()
    video_id = models.CharField()