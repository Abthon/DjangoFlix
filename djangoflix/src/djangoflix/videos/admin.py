from django.contrib import admin
from .models import Video


class VideoManager(admin.ModelAdmin):
    list_display = ["id","title","is_published","published_date"]
    list_filter = ["id","active"]
    readonly_fields = ["id","timestamp","updated"]
    
# Register your models here.
admin.site.register(Video,VideoManager)