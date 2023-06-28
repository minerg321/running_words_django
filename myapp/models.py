from django.db import models

class VideoRequest(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
