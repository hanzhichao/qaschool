import os

import markdown
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import send_mail


from qaschool import settings
from .forms import MDEditorForm, CKEditorForm
from .models import Category, Course, Lesson
from resource.models import ResCategory
from account.forms import LoginForm



def common():
    categories = Category.objects.all()
    res_categories = ResCategory.objects.all()
    login_form = LoginForm()
    return {'categories': categories, 'res_categories': res_categories, 'login_form': login_form}


def index(request):
    courses = Course.objects.all()
    locals().update(common())
    return render(request, 'courses/index.html', locals())


def category_detail(request, category_slug):
    categories = Category.objects.all()

    category = get_object_or_404(Category, slug=category_slug, visible=True)
    courses = Course.objects.filter(category=category)
    locals().update(common())
    return render(request, 'courses/category.html', locals())

def category_all(request):
    courses = Course.objects.all()
    locals().update(common())
    return render(request, 'courses/category_all.html', locals())


def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug, visible=True)
    lesson_one = Lesson.objects.filter(course=course).first()

    if lesson_one:
        return lesson_detail(request, course.slug, lesson_one.slug)

    lessons = Lesson.objects.filter(course=course)

    locals().update(common())
    return render(request, 'courses/course.html', locals())


def lesson_detail(request, course_slug, lesson_slug):
    course = get_object_or_404(Course, slug=course_slug)

    lessons = Lesson.objects.filter(course=course)
    lesson = get_object_or_404(Lesson, course=course, slug=lesson_slug, visible=True)
    lesson.viewed()

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

    locals().update(common())
    return render(request, 'courses/lesson.html', locals())


def search(request, keyword):
    categories = Category.objects.all()
    courses = Course.objects.all()

    category_result = categories.filter(title__icontains=keyword)
    course_result = courses.filter(title__icontains=keyword)
    lesson_result = Lesson.objects.filter(status='p', title__icontains=keyword)
    result_num = category_result.count() + course_result.count() + lesson_result.count()
    locals().update(common())
    return render(request, 'courses/search.html',  locals())

# def lesson_share(request, course_slug, lesson_slug):
#     course = get_object_or_404(Course, slug=course_slug)
#     lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course, status='p')
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         notes = request.POST.get('notes')
#         url = request.build_absolute_uri()[:-7]
#         subject = 'QA学院邮件分享'
#         msg = '课程：{}\n标题：{}\n链接：{}\n我的笔记：\n{}'.format(course.title, lesson.title, url, notes)
#         send_mail(subject, msg, 'ivan-me@163.com', [email])
#         return HttpResponse('邮件已发送')
#     return HttpResponse('不支持GET方法')



# @csrf_exempt
# def course_eval(request, course_slug):
#     if request.method == 'POST':
#         star = request.POST.get('star')
#         course = get_object_or_404(Course, slug=course_slug)
#         total = course.star_eval_num * course.star
#         course.star_eval_num += 1
#         course.star = (total + int(star))/course.star_eval_num
#         course.save()
#
#     return HttpResponse("评论成功")


# @csrf_exempt
# def add_likes(request, lesson_slug):
#     lesson = Lesson.objects.filter(slug=lesson_slug, status='p')
#     if not lesson:
#         return HttpResponse("没有找到相关章节")
#
#     lesson[0].likes += 1;
#     lesson[0].save()
#     return HttpResponse("点赞成功")

# # Create your views here.
# def lesson_edit(request):
#     form = MDEditorForm()
#     form2 = CKEditorForm()
#     return render(request, 'courses/lesson_edit.html', {"form": form, 'form2': form2})