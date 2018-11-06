from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import url

from .views import upload_image

urlpatterns = [
    url(r'^upload/$', upload_image, name='upload'),
]
