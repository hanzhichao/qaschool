from django.urls import path
from course import views


urlpatterns = [
    path('<column_slug>', views.column_detail, name='column'),
    path('course/<course_slug>', views.course_detail, name='course'),
    path('chapter/<chapter_slug>.html', views.chapter_detail, name='chapter'),
    path('<course_slug>/<chapter_slug>.html', views.chapter_detail, name='chapter'),
]
