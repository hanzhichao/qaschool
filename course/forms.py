from django import forms
from .models import Column, Course, Chapter


class ChapterAdminForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('abstract',)
        widgets = {
            'intro': forms.Textarea(attrs={'rows': "3", "style": "resize:none;"})
        }


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)