from django.db import models

class Video(models.Model):
    id
    videoid = models.CharField(max_length=50)
    url     = models.URLField()
    
    def __unicode__(self):
        return self.videoid
    
    