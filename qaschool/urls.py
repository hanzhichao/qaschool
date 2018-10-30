from django.contrib import admin
from django.urls import path
from django.conf import settings
from course import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<column_slug>', views.column_detail, name='column'),
    path('course/<course_slug>', views.course_detail, name='course'),
    path('chapter/<chapter_slug>', views.chapter_detail, name='chapter'),
    path('<course_slug>/<chapter_slug>', views.chapter_detail2, name='chapter2'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)