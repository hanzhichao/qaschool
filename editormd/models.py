import os
import uuid

from django.db import models
from django.utils import timezone

from editormd.settings import UPLOAD_TO
from .fields import EditorMdFormField


class EditorMdField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': EditorMdFormField}
        defaults.update(kwargs)
        return super(EditorMdField, self).formfield(**defaults)


def get_file_path(instance, filename):
    today = timezone.now()
    today_path = today.strftime("/%Y/%m/")
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(UPLOAD_TO + today_path, filename)


class Image(models.Model):
    image_file = models.ImageField(upload_to=get_file_path)
    author = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
