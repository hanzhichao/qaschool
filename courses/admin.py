from django.contrib import admin
from .models import Category, Course, Lesson

admin.site.site_header = 'QA School后台管理系统'
admin.site.site_title = 'QA School后台管理系统'


class CategoryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    fields = ('title', 'slug', ('owner', 'order'), 'keywords', 'description')
    list_display = ('title', 'order', 'visible', 'owner', 'created', 'updated')
    list_filter = ('visible', 'owner')
    list_editable = ['order', 'visible']


class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(CourseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    fields = ('title', 'slug', ('category', 'owner', 'is_suggest'), 'pic', 'keywords', 'description')
    list_display = ('title', 'category', 'order', 'visible', 'is_suggest', 'owner', 'created', 'updated')
    list_filter = ('category', 'visible', 'is_suggest', 'owner')
    list_editable = ['order', 'visible', 'is_suggest']



class LessonAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(LessonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    fields = ('title', 'slug', ('course', 'owner'), 'keywords', 'description', 'md_content', 'html_content')
    list_display = ('title', 'course', 'order', 'visible', 'owner', 'created', 'updated')
    list_filter = ('course', 'visible', 'owner')
    list_editable = ['visible']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)