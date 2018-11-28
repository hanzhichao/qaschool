from django.shortcuts import render, get_object_or_404
from .models import  Category, Content
# Create your views here.

def category_all(request):
    categories = Category.objects.filter(visible=True)
    contents = Content.objects.filter(status='p')

    return render(request, 'resource/category_all.html', {'categories': categories, 'contents': contents})


def content_list(request, category_slug):
    categories = Category.objects.filter(visible=True)
    category = Category.objects.filter(visible=True, slug=category_slug)
    contents = Content.objects.filter(status='p', category=category)

    return render(request, 'resource/content_list.html', {'categories': categories,
                                                          'category': category, 'contents': contents})


def content_detail(request, category_slug, content_slug):
    category = get_object_or_404(Category, visible=True, slug=category_slug)
    content = get_object_or_404(Content, status='p', category=category, slug=category)
    return render(request, 'resource/content_detail.html', {'category': category, 'content': content})