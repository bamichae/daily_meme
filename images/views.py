import logging

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from images.forms import UploadForm
from images.models import Image
from images.tables import ImageTable



logger = logging.getLogger(__name__)


def index_view(request):
    images = Image.objects.all()
    image_table = ImageTable(images)
    upload_form = UploadForm()

    return render(request, 'images/override.html', {
        'images': images,
        'image_table': image_table,
        'upload_form': upload_form,
    })

def test_view(request):
    # Get the newest image
    image = Image.objects.order_by('-pk')[0]
    return render(request, "images/index.html", {
        'image': image})


@require_http_methods(["POST"])
def upload_view(request):
    upload_form = UploadForm(data=request.POST, files=request.FILES)

    if upload_form.is_valid():
        upload_form.save(commit=True)
        return redirect('test-upload')
    else:
        logger.warning("Something went wrong with uploading the file.")
        logger.warning(request.POST)
        logger.warning(request.FILES)

    return redirect('images-index')
