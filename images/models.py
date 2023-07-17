import sys

from django.db import models
import logging

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_daily_meme = models.BooleanField(default=False)

    class Meta:
        ordering = ['-uploaded_at']

