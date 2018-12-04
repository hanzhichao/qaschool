from django.urls import path

from courses import views


urlpatterns = [
    # path('', views.lesson_edit, name='lesson_edit'),
    path('category/<category_slug>', views.category_detail, name='category'),
    path('all/', views.category_all, name='category_all'),
    path('<course_slug>', views.course_detail, name='course'),
    # path('<lesson_slug>.html', views.lesson_detail, name='lesson'),
    path('<course_slug>/<lesson_slug>.html', views.lesson_detail, name='lesson'),
    path('search/<keyword>', views.search, name='search'),
    # path('eval/<course_slug>', views.course_eval, name='course_eval'),
    # path('add_likes/<lesson_slug>', views.add_likes, name='add_likes'),
    # path('api/course/add', views.course_add, name='course_add'),
    # path('api/lesson/add', views.lesson_add, name='lesson_add'),
]