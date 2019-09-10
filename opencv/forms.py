from django import forms
from .models import Image


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',) 