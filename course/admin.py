from django.contrib import admin
from .models import Column, Course, Lesson
from .forms import ArticleAdminForm


admin.site.site_header = 'QAschool后台管理系统'
admin.site.site_title = 'QAschool后台管理系统'


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'pre_column', 'intro')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'column', 'intro')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'last_modified_time')
    form = ArticleAdminForm
    fields = ('title', 'slug', 'course', 'abstract', 'content')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, ArticleAdmin)

