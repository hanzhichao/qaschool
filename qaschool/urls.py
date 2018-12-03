from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from courses import views
from django.views.generic import RedirectView


urlpatterns = [
    path('account/', include('account.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('han/', admin.site.urls),
    path('', views.index, name='index'),
    path('courses/', include('courses.urls')),
    path('resource/', include('resource.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

