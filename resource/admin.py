from django.contrib import admin
from .models import Category, Content


class CategoryAdmin(admin.ModelAdmin):
    pass


class ContentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
