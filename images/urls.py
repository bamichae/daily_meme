import threading

from django.urls import path

from . import views

urlpatterns = [
    path('override', views.index_view, name='images-index'),
    path('upload', views.upload_view, name='images-upload'),
    path('', views.test_view, name='test-upload'),
]

from .models import Image
def refresh_daily_meme(counter):
    """
    Timer which waits 24 hours before starting a thread which refreshes the daily meme
    :param counter:
    :return:
    """
    image = Image(file=f'images/{counter}.png')
    image.save()
    counter += 1
    seconds_in_a_day = 86400
    threading.Timer(seconds_in_a_day, refresh_daily_meme, args=[counter,]).start()

# Populate the db with the first image right away
image = Image(file=f'images/0.png')
image.save()
threading.Timer(60 * 60 * 8, refresh_daily_meme, args=[1,]).start()

