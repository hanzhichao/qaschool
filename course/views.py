from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template.loader import render_to_string
from .models import Column, Course, Chapter, Comment, Config
# from .forms import EmailPostForm
import markdown
import os
from qaschool import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


def _get_theme_css():
    config = Config.objects.filter(name='默认')
    if config and config[0].theme:
        return 'css/{}.css'.format(config[0].theme)
    return 'css/{}.css'.format(settings.THEME)


def _get_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']


def index(request):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')

    return render(request, 'course/index.html', {'columns': columns, 'courses': courses, 'theme_css': _get_theme_css()})


def column_detail(request, column_slug):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')

    column = Column.objects.filter(slug=column_slug)
    if column:
        column = column[0]
    cur_courses = Course.objects.filter(column=column, visible=True).order_by('sn')
    return render(request, 'course/column.html', {'column': column, 'cur_courses': cur_courses, 'columns': columns,
                                                  'courses': courses, 'theme_css': _get_theme_css()})

def course_all(request):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')

    return render(request, 'course/course_all.html', {'columns': columns,
                                                  'courses': courses, 'theme_css': _get_theme_css()})


def course_detail(request, course_slug):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')

    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapter_one = Chapter.objects.filter(course=course, status='p').order_by('sn').first()

    # if chapter_one:
    #     return chapter_detail(request, course.slug, chapter_one.slug)

    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    return render(request, 'course/course.html', {'course': course, 'chapters': chapters, 'columns': columns,
                                                  'courses': courses, 'theme_css': _get_theme_css()})


def chapter_detail(request, course_slug, chapter_slug):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')

    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    chapter = Chapter.objects.filter(course=course, slug=chapter_slug, status='p')
    if chapter:
        chapter = chapter[0]

    # 获取上一篇，下一篇
    chapter_list = list(chapters)
    cur_index = chapter_list.index(chapter)
    if cur_index == 0:
        pre_chapter = None
    else:
        pre_chapter = chapter_list[cur_index - 1]

    if chapter == chapter_list[-1]:
        next_chapter = None
    else:
        next_chapter = chapter_list[cur_index+1]

    # 浏览量 + 1
    chapter.views += 1
    chapter.save()

    chapter.content = markdown.markdown(chapter.content.replace("\r\n", '  \n'), extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])
    # 评论
    comments = chapter.comments.filter(visible=True)

    # 生成静态页面
    # config = Config.objects.filter(name='默认')
    # if config and config.gen_static_pages:
    if settings.STATIC_PAGES:
        static_html = os.path.join(settings.BASE_DIR, 'pages', 'course', '{}.html'.format(chapter.slug))

        if not os.path.exists(static_html):
            tpl = os.path.join(settings.TEMPLATES[0]['DIRS'][0], 'course', 'column.html')
            content = render_to_string(tpl, {'chapter': chapter, 'course': course, 'chapters': chapters,
                                             'columns': columns, 'courses': courses, 'theme_css': _get_theme_css(),
                                             'comments': comments, 'pre_chapter': pre_chapter,
                                             'next_chapter': next_chapter})
            with open(static_html, 'w', encoding='utf-8') as static_file:
                static_file.write(content)
        return render(request, static_html)
    else:
        return render(request, 'course/column.html', {'chapter': chapter, 'course': course, 'chapters': chapters,
                                                       'columns': columns, 'courses': courses, 'theme_css': _get_theme_css(),
                                                       'comments': comments, 'pre_chapter': pre_chapter,
                                                       'next_chapter': next_chapter})


def search(request, keyword):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')

    column_result = columns.filter(name__icontains=keyword).order_by('sn')
    course_result = courses.filter(name__icontains=keyword).order_by('sn')
    chapter_result = Chapter.objects.filter(status='p', title__icontains=keyword).order_by('sn')
    result_num = column_result.count() + course_result.count() + chapter_result.count()

    return render(request, 'course/search.html',  {'columns': columns, 'courses': courses, 'theme_css': _get_theme_css(),
                                                   'column_result': column_result, 'course_result': course_result,
                                                   'chapter_result': chapter_result, 'result_num': str(result_num)})


def chapter_share(request, course_slug, chapter_slug):
    course = get_object_or_404(Course, slug=course_slug, visible=True)
    chapter = get_object_or_404(Chapter, slug=chapter_slug, course=course, status='p')
    if request.method == 'POST':
        email = request.POST.get('email')
        notes = request.POST.get('notes')
        url = request.build_absolute_uri()[:-7]
        subject = 'QA学院邮件分享'
        msg = '课程：{}\n标题：{}\n链接：{}\n我的笔记：\n{}'.format(course.name, chapter.title, url, notes)
        send_mail(subject, msg, 'ivan-me@163.com', [email])
        return HttpResponse('邮件已发送')
    return HttpResponse('不支持GET方法')


def comment_add(request, course_slug, chapter_slug):
    course = get_object_or_404(Course, slug=course_slug, visible=True)      # ToDo 
    chapter = get_object_or_404(Chapter, slug=chapter_slug, course=course, status='p')  # ToDo 
    if request.method == 'POST':
        name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        content = request.POST.get('comment_content')
        comment = Comment(name=name, email=email, content=content, chapter=chapter)
        comment.save()
        return HttpResponse('评论已添加')
    return HttpResponse('不支持GET方法')


@csrf_exempt
def course_eval(request, course_slug):
    if request.method == 'POST':
        star = request.POST.get('star')
        course = get_object_or_404(Course, slug=course_slug, visible=True)
        total = course.star_eval_num * course.star
        course.star_eval_num += 1
        course.star = (total + int(star))/course.star_eval_num
        course.save()

    return HttpResponse("评论成功")


@csrf_exempt
def add_likes(request, chapter_slug):
    chapter = Chapter.objects.filter(slug=chapter_slug, status='p')
    if not chapter:
        return HttpResponse("没有找到相关章节")

    chapter[0].likes += 1;
    chapter[0].save()
    return HttpResponse("点赞成功")

