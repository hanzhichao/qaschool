from django.shortcuts import render, get_object_or_404
from .models import  ItemCategory, ItemContent

from courses.views import common

def item_category_all(request):
    item_categories = ItemCategory.objects.all()
    item_contents = ItemContent.objects.all()
    locals().update(common())
    return render(request, 'practice/item_category_all.html', locals())


def item_category(request, item_category_slug):
    item_categories = ItemCategory.objects.all()
    item_category = get_object_or_404(ItemCategory, visible=True, slug=item_category_slug)
    item_contents = ItemContent.objects.filter(category=item_category)
    locals().update(common())
    return render(request, 'practice/item_category.html', locals())


def item_content_detail(request, item_category_slug, item_content_slug):
    item_categories = ItemCategory.objects.all()
    item_category = get_object_or_404(ItemCategory, visible=True, slug=item_category_slug)
    item_content = get_object_or_404(ItemContent, category=item_category, slug=item_content_slug)
    item_content.viewed()
    locals().update(common())
    return render(request, 'practice/item_content_detail.html', locals())