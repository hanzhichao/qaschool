from django.contrib import admin
from .models import Column, Course, Chapter, Comment, Config
from .forms import ChapterAdminForm


admin.site.site_header = 'QA School后台管理系统'
admin.site.site_title = 'QA School后台管理系统'


class CourseInline(admin.TabularInline):  # admin.StackedInline
    model = Course


class ColumnAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ColumnAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manager=request.user)

    list_display = ('name', 'sn', 'visible', 'show_in_nav', 'manager', 'created_time', 'last_modified_time')
    list_filter = ('visible', )
    fields = ('name', 'manager', 'slug', 'intro')
    list_editable = ['sn', 'visible', 'show_in_nav']
    inlines = [CourseInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sn', 'column', 'visible', 'author', 'created_time', 'last_modified_time')
    list_filter = ('column', 'author', 'visible')
    list_editable = ['sn', 'visible']


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'sn', 'course', 'views', 'status', 'created_time', 'last_modified_time')
    form = ChapterAdminForm
    fields = ('title', 'sn', 'slug', 'course', 'abstract', 'content', 'html_content', 'status')
    list_filter = ('course', 'status')
    ordering = ('sn',)
    list_editable = ['sn', 'status']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'name', 'email', 'visible', 'content', 'created_time')
    list_filter = ('visible', 'created_time', 'last_modified_time')
    search_fields = ('name', 'email', 'content')
    list_editable = ['visible']


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'template', 'theme', 'gen_static_pages')
    # fields = ('template', 'theme', 'gen_static_pages')
    # readonly_fields = ('name',)


admin.site.register(Column, ColumnAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Config, ConfigAdmin)

