from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, get_object_or_404


from .models import Category, Course, Lesson, Comment

@csrf_exempt
def course_add(request):
    category = Category.objects.first()
    if request.method == "POST":
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        description = request.POST.get('description')
        course = Course(category=category, title=title, slug=slug, description=description, owner_id=1)
        course.save()
        return HttpResponse("添加成功")
    return HttpResponse("不支持GET")


@csrf_exempt
def lesson_add(request):
    if request.method == "POST":
        course_slug = request.POST.get("course_slug")
        course = get_object_or_404(Course, slug=course_slug)
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        html_content = request.POST.get('html_content')
        lesson = Lesson(course=course, title=title, slug=slug, html_content=html_content, owner_id=1)
        lesson.save()
        return HttpResponse("添加成功")
    return HttpResponse("不支持GET")
