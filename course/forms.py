from django import forms
from .models import Column, Course, Lesson


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('abstract',)
        widgets = {
            'intro': forms.Textarea(attrs={'rows': "3", "style": "resize:none;"})
        }