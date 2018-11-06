from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from course import views
from django.views.generic import RedirectView

urlpatterns = [
    path('mdeditor/', include('mdeditor.urls')),
    path('cactus/', admin.site.urls),
    path('', views.index, name='index'),
    path('course/', include('course.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico'))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
