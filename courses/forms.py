from django import forms
from mdeditor.fields import MDTextFormField
from django.forms import widgets
from django.forms import fields

from .models import Lesson

# class MDEditorForm(forms.Form):
#     name = fields.CharField(widget=widgets.TextInput(attrs={"class":"form-control"}))
#     content = MDTextFormField()

class MDEditorForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'md_content')
    # name = fields.CharField(widget=widgets.TextInput(attrs={"class":"form-control"}))
    # content = MDTextFormField()



class CKEditorForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'html_content')


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


