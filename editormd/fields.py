from django import forms
from .widgets import EditorMdWidget


class EditorMdFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(EditorMdFormField, self).__init__(*args, **kwargs)
        self.widget = EditorMdWidget()
