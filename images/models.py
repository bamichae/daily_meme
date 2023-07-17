import sys

from django.db import models
import logging

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def is_daily_meme(self):
        """
        Assumption here is the database will save alphanumeric images and we saved digits.
        In the future, a seperate page should be rendered for the daily meme vs overriden meme and
        returned accordingly.
        :return:
        """
        path_name = self.file.name.split('.')[0]
        image_name = path_name.split('/')[1]
        if image_name.isdigit():
            return False
        else:
            return True

    class Meta:
        ordering = ['-uploaded_at']

