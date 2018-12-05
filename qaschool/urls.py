from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from courses import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('han/', admin.site.urls),

    path('mdeditor/', include('mdeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', views.index, name='index'),

    path('account/', include('account.urls')),
    path('courses/', include('courses.urls')),
    path('resource/', include('resource.urls')),
    path('practice/', include('practice.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

