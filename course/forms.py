from django import forms
from .models import Column, Course, Chapter


class ChapterAdminForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('abstract',)
        widgets = {
            'intro': forms.Textarea(attrs={'rows': "3", "style": "resize:none;"})
        }