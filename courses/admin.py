from django.contrib import admin
from .models import Category, Course, Lesson


class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'keywords', ('owner', 'order'), 'description')


class CourseAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'keywords', ('category', 'owner', 'order'), 'description')



class LessonAdmin(admin.ModelAdmin):
    # pass
    fields = ('title', 'slug', 'keywords', ('module', 'owner','status','order'), 'description', 'md_content', 'html_content')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)