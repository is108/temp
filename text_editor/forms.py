from django import forms

from .models import Text
from .models import Image

class TextForm(forms.ModelForm):

    class Meta:
        model = Text
        fields = ('text',)


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)

class FileForm(forms.Form):
    file = forms.FileField()
