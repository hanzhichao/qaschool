from django.urls import path
from course import views


urlpatterns = [
    path('column/<column_slug>', views.column_detail, name='column'),
    path('<course_slug>', views.course_detail, name='course'),
    # path('<chapter_slug>.html', views.chapter_detail, name='chapter'),
    path('<course_slug>/<chapter_slug>.html', views.chapter_detail, name='chapter'),
    path('<course_slug>/<chapter_slug>.html/share/', views.chapter_share, name='chapter_share'),
    path('<course_slug>/<chapter_slug>.html/comment_add/', views.comment_add, name='comment_add'),
    path('search/<keyword>', views.search, name='search'),
]
