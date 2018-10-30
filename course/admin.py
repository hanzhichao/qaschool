from django.contrib import admin
from .models import Column, Course, Chapter
from .forms import ChapterAdminForm


admin.site.site_header = 'QA School后台管理系统'
admin.site.site_title = 'QA School后台管理系统'


class ColumnAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ColumnAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manager=request.user)

    list_display = ('name', 'pre_column', 'visible', 'manager', 'created_time', 'last_modified_time')
    list_filter = ('visible', )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'column', 'visible', 'author', 'created_time', 'last_modified_time')
    list_filter = ('column', 'author', 'visible')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'sn', 'course', 'views', 'visible', 'created_time', 'last_modified_time')
    form = ChapterAdminForm
    fields = ('title', 'sn', 'slug', 'course', 'abstract', 'content')
    list_filter = ('course', 'visible')
    ordering = ('sn',)
    list_editable = ['sn', 'visible']


admin.site.register(Column, ColumnAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)

