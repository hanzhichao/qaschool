from django.contrib import admin
from django.urls import path
from django.conf import settings
from course import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<column_slug>', views.column_detail, name='column'),
    path('course/<course_slug>', views.course_detail, name='course'),
    path('article/<article_slug>', views.article_detail, name='article'),
    path('<course_slug>/<article_slug>', views.article_detail2, name='article2'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)