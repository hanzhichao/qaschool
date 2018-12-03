import os

import markdown
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from qaschool import settings
from .forms import MDEditorForm, CKEditorForm
from .models import Category, Course, Lesson



def index(request):
    categories = Category.objects.all()
    courses = Course.objects.filter()
    return render(request, 'courses/index.html', {'categories': categories, 'courses': courses})


def category_detail(request, category_slug):
    categories = Category.objects.all()
    courses = Course.objects.all()

    category = Category.objects.filter(slug=category_slug)
    if category:
        category = category[0]
    cur_courses = Course.objects.filter(category=category)
    return render(request, 'courses/category.html', {'category': category, 'cur_courses': cur_courses, 'categories': categories,
                                                  'courses': courses})

def course_all(request):
    categories = Category.objects.all().order_by('order')
    courses = Course.objects.all().order_by('order')

    return render(request, 'courses/course_all.html', {'categories': categories,
                                                  'courses': courses})

def course_detail(request, course_slug):
    categories = Category.objects.all().order_by('order')
    courses = Course.objects.all().order_by('order')

    course = Course.objects.filter(slug=course_slug)
    if course:
        course = course[0]
    lesson_one = Lesson.objects.filter(course=course, status='p').order_by('order').first()

    if lesson_one:
        return lesson_detail(request, course.slug, lesson_one.slug)

    lessons = Lesson.objects.filter(course=course, status='p').order_by('order')
    return render(request, 'courses/course.html', {'course': course, 'lessons': lessons, 'categories': categories,
                                                  'courses': courses})


def lesson_detail(request, course_slug, lesson_slug):
    categories = Category.objects.all().order_by('order')
    courses = Course.objects.all().order_by('order')

    course = Course.objects.filter(slug=course_slug)
    if course:
        course = course[0]
    lessons = Lesson.objects.filter(course=course, status='p').order_by('order')
    lesson = Lesson.objects.filter(course=course, slug=lesson_slug, status='p')
    if lesson:
        lesson = lesson[0]

    # 获取上一篇，下一篇
    lesson_list = list(lessons)
    cur_index = lesson_list.index(lesson)
    if cur_index == 0:
        pre_lesson = None
    else:
        pre_lesson = lesson_list[cur_index - 1]

    if lesson == lesson_list[-1]:
        next_lesson = None
    else:
        next_lesson = lesson_list[cur_index+1]


    if lesson.html_content:
        lesson.content = lesson.html_content
    elif lesson.md_content:
        lesson.content = markdown.markdown(lesson.md_content.replace("\r\n", '  \n'),
                                            extensions=['markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc', ])
    else:
        lesson.content = ''



    return render(request, 'courses/lesson.html', {'lesson': lesson, 'course': course, 'lessons': lessons,
                                                       'categories': categories, 'courses': courses,'pre_lesson': pre_lesson,
                                                       'next_lesson': next_lesson})


def search(request, keyword):
    categories = Category.objects.all().order_by('order')
    courses = Course.objects.all().order_by('order')

    category_result = categories.filter(title__icontains=keyword).order_by('order')
    course_result = courses.filter(title__icontains=keyword).order_by('order')
    lesson_result = Lesson.objects.filter(status='p', title__icontains=keyword).order_by('order')
    result_num = category_result.count() + course_result.count() + lesson_result.count()

    return render(request, 'courses/search.html',  {'categories': categories, 'courses': courses,
                                                   'category_result': category_result, 'course_result': course_result,

                                                   'lesson_result': lesson_result, 'result_num': str(result_num)})
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

def lesson_share(request, course_slug, lesson_slug):
    course = get_object_or_404(Course, slug=course_slug)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course, status='p')
    if request.method == 'POST':
        email = request.POST.get('email')
        notes = request.POST.get('notes')
        url = request.build_absolute_uri()[:-7]
        subject = 'QA学院邮件分享'
        msg = '课程：{}\n标题：{}\n链接：{}\n我的笔记：\n{}'.format(course.title, lesson.title, url, notes)
        send_mail(subject, msg, 'ivan-me@163.com', [email])
        return HttpResponse('邮件已发送')
    return HttpResponse('不支持GET方法')



@csrf_exempt
def course_eval(request, course_slug):
    if request.method == 'POST':
        star = request.POST.get('star')
        course = get_object_or_404(Course, slug=course_slug)
        total = course.star_eval_num * course.star
        course.star_eval_num += 1
        course.star = (total + int(star))/course.star_eval_num
        course.save()

    return HttpResponse("评论成功")


@csrf_exempt
def add_likes(request, lesson_slug):
    lesson = Lesson.objects.filter(slug=lesson_slug, status='p')
    if not lesson:
        return HttpResponse("没有找到相关章节")

    lesson[0].likes += 1;
    lesson[0].save()
    return HttpResponse("点赞成功")

# Create your views here.
def lesson_edit(request):
    form = MDEditorForm()
    form2 = CKEditorForm()
    return render(request, 'courses/lesson_edit.html', {"form": form, 'form2': form2})