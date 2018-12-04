from django.shortcuts import render, get_object_or_404
from .models import  ResCategory, ResContent

from courses.views import common

def res_category_all(request):
    res_categories = ResCategory.objects.all()
    res_contents = ResContent.objects.all()
    locals().update(common())
    return render(request, 'resource/res_category_all.html', locals())


def res_category(request, res_category_slug):
    res_categories = ResCategory.objects.all()
    res_category = get_object_or_404(ResCategory, visible=True, slug=res_category_slug)
    res_contents = ResContent.objects.filter(category=res_category)
    locals().update(common())
    return render(request, 'resource/res_category.html', locals())


def res_content_detail(request, res_category_slug, res_content_slug):
    res_categories = ResCategory.objects.all()
    res_category = get_object_or_404(ResCategory, visible=True, slug=res_category_slug)
    res_content = get_object_or_404(ResContent, category=res_category, slug=res_content_slug)
    locals().update(common())
    return render(request, 'resource/res_content_detail.html', locals())