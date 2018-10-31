from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from course import views


urlpatterns = [
    path('mdeditor/', include('mdeditor.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('course/', include('course.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
