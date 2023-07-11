from django import forms

from images.models import Image


class UploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['file']
        labels = {
            'file': "Image",
        }
