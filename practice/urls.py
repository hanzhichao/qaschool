from django.urls import path
from practice import views

namespace = 'practice'
urlpatterns = [
    path('', views.item_category_all, name='item_category_all'),
    path('<item_category_slug>', views.item_category, name='item_category'),
    path('<item_category_slug>/<item_content_slug>.html', views.item_content_detail, name='item_content'),
]
