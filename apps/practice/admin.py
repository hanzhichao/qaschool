from django.contrib import admin
from .models import ItemCategory, ItemContent


class ItemCategoryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ItemCategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    fields = ('title', 'slug', ('owner', 'order'), 'keywords', 'description')
    list_display = ('title', 'order', 'visible', 'owner', 'created', 'updated')
    list_filter = ('visible', 'owner')
    list_editable = ['order', 'visible']



class ItemContentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ItemContentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    fields = ('title', 'slug', ('category', 'owner'), 'keywords', 'description', 'answer')
    list_display = ('title', 'category', 'order', 'visible', 'owner', 'created', 'updated')
    list_filter = ('category', 'visible', 'owner')
    list_editable = ['visible']



admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemContent, ItemContentAdmin)
