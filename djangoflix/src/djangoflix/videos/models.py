from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISH = 'PU', 'Publish'
        
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=300,null=True,blank=True,default="abc")
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(choices=VideoStateOptions.choices, max_length=200, default=VideoStateOptions.DRAFT)
    published_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    
    
    def save(self,*args, **kwargs):
        if(self.state == Video.VideoStateOptions.PUBLISH and self.published_timestamp is None):
            self.published_timestamp = timezone.now()
        elif(self.state == Video.VideoStateOptions.DRAFT and self.published_timestamp is not None):
            self.published_timestamp = None
        if self.slug is None:
            self.slug = slugify(self.title) 
        
        super().save(*args, **kwargs)
    
    @property
    def is_published(self):
        return self.active
    
    @property
    def published_date(self):
        return self.published_timestamp
    
    def __self__(self):
        return self.title
    

class VideoQuerySet(models.QuerySet):
    pass
    
class VideoProxy(Video):
    class Meta:
        proxy = True
    