from django.urls import path
from resource import views

# app_name = 'resource'
urlpatterns = [
    path('all/', views.category_all, name='category_all'),
    path('<category_slug>', views.content_list, name='content_list'),
    path('<category_slug>/<content_slug>.html', views.content_detail, name='content_detail'),
]
