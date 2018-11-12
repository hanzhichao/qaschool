from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template.loader import render_to_string
from .models import Column, Course, Chapter, Comment
# from .forms import EmailPostForm
import markdown
import os
from qaschool import settings
from django.core.mail import send_mail


def index(request):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')
    theme_css = 'css/{}.css'.format(settings.THEME)
    return render(request, 'course/index.html', {'columns': columns, 'courses': courses, 'theme_css': theme_css})


def column_detail(request, column_slug):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')
    theme_css = 'css/{}.css'.format(settings.THEME)
    column = Column.objects.filter(slug=column_slug)
    if column:
        column = column[0]
    cur_courses = Course.objects.filter(column=column, visible=True).order_by('sn')
    return render(request, 'course/column.html', {'column': column, 'cur_courses': cur_courses, 'columns': columns,
                                                  'courses': courses, 'theme_css': theme_css})


def course_detail(request, course_slug):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')
    theme_css = 'css/{}.css'.format(settings.THEME)
    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapter_one = Chapter.objects.filter(course=course, status='p').order_by('sn').first()

    if chapter_one:
        return chapter_detail(request, course.slug, chapter_one.slug)

    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    return render(request, 'course/course.html', {'course': course, 'chapters': chapters, 'columns': columns,
                                                  'courses': courses, 'theme_css': theme_css})


def chapter_detail(request, course_slug, chapter_slug):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')
    theme_css = 'css/{}.css'.format(settings.THEME)
    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    chapter = Chapter.objects.filter(course=course, slug=chapter_slug, status='p')
    if chapter:
        chapter = chapter[0]

    # 获取上一篇，下一篇
    chapter_list = list(chapters)
    if chapter == chapter_list[0]:
        pre_chapter = None
        next_chapter = chapter_list[1]
    elif chapter == chapter_list[-1]:
        pre_chapter = chapter_list[-2]
        next_chapter = None
    else:
        cur_index = chapter_list.index(chapter)
        pre_chapter = chapter_list[cur_index-1]
        next_chapter = chapter_list[cur_index+1]

    # 浏览量 + 1
    chapter.views += 1
    chapter.save()

    chapter.content = markdown.markdown(chapter.content, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])
    # 评论
    comments = chapter.comments.filter(visible=True)

    # 生成静态页面
    if not settings.STATIC_PAGES:
        return render(request, 'course/chapter.html', {'chapter': chapter, 'course':course, 'chapters': chapters,
                                                       'columns': columns, 'courses': courses, 'theme_css': theme_css,
                                                       'comments': comments, 'pre_chapter': pre_chapter,
                                                       'next_chapter': next_chapter})
    else:

        static_html = os.path.join(settings.BASE_DIR, 'pages', 'course', '{}.html'.format(chapter.slug))

        if not os.path.exists(static_html):
            tpl = os.path.join(settings.TEMPLATES[0]['DIRS'][0], 'course', 'chapter.html')
            content = render_to_string(tpl, {'chapter': chapter, 'course':course, 'chapters': chapters,
                                             'columns': columns, 'courses': courses, 'theme_css': theme_css,
                                             'comments': comments, 'pre_chapter': pre_chapter,
                                             'next_chapter': next_chapter})
            with open(static_html, 'w', encoding='utf-8') as static_file:
                static_file.write(content)
        return render(request, static_html)


def search(request, keyword):
    columns = Column.objects.filter(visible=True).order_by('sn')
    courses = Course.objects.filter(visible=True).order_by('sn')
    theme_css = 'css/{}.css'.format(settings.THEME)
    column_result = columns.filter(name__icontains=keyword).order_by('sn')
    course_result = courses.filter(name__icontains=keyword).order_by('sn')
    chapter_result = Chapter.objects.filter(status='p', title__icontains=keyword).order_by('sn')
    result_num = column_result.count() + course_result.count() + chapter_result.count()

    return render(request, 'course/search.html',  {'columns': columns, 'courses': courses, 'theme_css': theme_css,
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
    course = get_object_or_404(Course, slug=course_slug, visible=True)
    chapter = get_object_or_404(Chapter, slug=chapter_slug, course=course, status='p')
    if request.method == 'POST':
        name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        content = request.POST.get('comment_content')
        comment = Comment(name=name, email=email, content=content, chapter=chapter)
        comment.save()
        return HttpResponse('评论已添加')
    return HttpResponse('不支持GET方法')


