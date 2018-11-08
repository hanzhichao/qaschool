from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template.loader import render_to_string
from .models import Column, Course, Chapter
from .forms import EmailPostForm
import markdown
import os
from qaschool import settings
from django.core.mail import send_mail



columns = Column.objects.filter(visible=True).order_by('sn')
courses = Course.objects.filter(visible=True).order_by('sn')

theme_css = 'css/{}.css'.format(settings.THEME)

def index(request):
    return render(request, 'course/index.html', {'columns': columns, 'courses': courses, 'theme_css': theme_css})


def column_detail(request, column_slug):
    column = Column.objects.filter(slug=column_slug)
    if column:
        column = column[0]
    cur_courses = Course.objects.filter(column=column, visible=True).order_by('sn')
    return render(request, 'course/column.html', {'column': column, 'cur_courses': cur_courses, 'columns': columns, 'courses': courses, 'theme_css': theme_css})


def course_detail(request, course_slug):
    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapter_one = Chapter.objects.filter(course=course, status='p').order_by('sn').first()

    if chapter_one:
        return chapter_detail(request, course.slug, chapter_one.slug)

    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    return render(request, 'course/course.html', {'course': course, 'chapters': chapters, 'columns': columns, 'courses': courses, 'theme_css': theme_css})


def chapter_detail(request, course_slug, chapter_slug):
    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapter = Chapter.objects.filter(course=course, slug=chapter_slug, status='p')
    if chapter:
        chapter = chapter[0]

    # 浏览量 + 1
    chapter.views += 1
    chapter.save()
    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    chapter.content = markdown.markdown(chapter.content, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])

    if not settings.STATIC_PAGES:
        return render(request, 'course/chapter.html', {'chapter': chapter, 'course':course, 'chapters': chapters, 'columns': columns, 'courses': courses, 'theme_css': theme_css})
    else:
        # 生成静态页面
        static_html = os.path.join(settings.BASE_DIR, 'pages', 'course', '{}.html'.format(chapter.slug))

        if not os.path.exists(static_html):
            tpl = os.path.join(settings.TEMPLATES[0]['DIRS'][0], 'course', 'chapter.html')
            content = render_to_string(tpl, {'chapter': chapter, 'course':course, 'chapters': chapters, 'columns': columns, 'courses': courses, 'theme_css': theme_css})
            with open(static_html, 'w', encoding='utf-8') as static_file:
                static_file.write(content)
        return render(request, static_html)

def chapter_share(request, chapter_slug):
    chapter = get_object_or_404(Chapter, slug=chapter_slug, status='p')
    sent = False
    cd = None
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # post_url = request.build_absolute_uri(chapter.get_absolute_url)
            post_url = chapter.get_absolute_url
            subject = '{} {} 推荐你阅读：{}'.format(cd['name'], cd['email'], chapter.title)
            msg = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(chapter.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, msg, 'ivan-me@163.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'course/share.html', {'chapter': chapter, 'form': form, 'sent': sent, 'cd': cd, 'theme_css': theme_css})

