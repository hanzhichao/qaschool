from django import forms


class ImageUploadForm(forms.Form):
    image_file = forms.ImageField()
