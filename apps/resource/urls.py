from django.urls import path
from resource import views


urlpatterns = [
    path('', views.res_category_all, name='res_category_all'),
    path('<res_category_slug>', views.res_category, name='res_category'),
    path('<res_category_slug>/<res_content_slug>.html', views.res_content_detail, name='res_content'),
]
