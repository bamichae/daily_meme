import threading

from django.urls import path

from . import views

urlpatterns = [
    path('override', views.index_view, name='images-index'),
    path('upload', views.upload_view, name='images-upload'),
    path('', views.test_view, name='test-upload'),
]

# TODO: This breaks python manage.py migrations; find a better place for it.
from .models import Image
def refresh_daily_meme(counter):
    """
    Timer which waits 24 hours before starting a thread which refreshes the daily meme
    :param counter:
    :return:
    """
    # Save the daily meme in db
    image = Image(file=f'images/{counter}.png')
    image.is_daily_meme = True
    image.save()

    # Increment counter and wait 24 hours
    counter += 1
    seconds_in_a_day = 86400
    threading.Timer(seconds_in_a_day, refresh_daily_meme, args=[counter,]).start()


# Populate the db with the first image right away
image = Image(file=f'images/0.png')
image.is_daily_meme = True
image.save()
time_to_12_am = 60 * 60 * 8
threading.Timer(time_to_12_am, refresh_daily_meme, args=[1,]).start()

