from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from course import views
from django.views.generic import RedirectView
from DjangoUeditor import urls as DjangoUeditor_urls

urlpatterns = [
    path('mdeditor/', include('mdeditor.urls')),
    path('han/', admin.site.urls),
    path(r'^ueditor/', include(DjangoUeditor_urls)),
    path('', views.index, name='index'),
    path('course/', include('course.urls')),
    path('account/', include('account.urls')),
    path('accounts/', include('users.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
