from django.contrib import admin
from .models import ResCategory, ResContent


class ResCategoryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ResCategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    fields = ('title', 'slug', ('owner', 'order'), 'keywords', 'description')
    list_display = ('title', 'order', 'visible', 'owner', 'created', 'updated')
    list_filter = ('visible', 'owner')
    list_editable = ['order', 'visible']



class ResContentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ResContentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    fields = ('title', 'slug', ('category', 'owner'), 'keywords', 'description', 'html_content')
    list_display = ('title', 'category', 'order', 'visible', 'owner', 'created', 'updated')
    list_filter = ('category', 'visible', 'owner')
    list_editable = ['visible']



admin.site.register(ResCategory, ResCategoryAdmin)
admin.site.register(ResContent, ResContentAdmin)
