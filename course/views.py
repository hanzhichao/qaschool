from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.template.loader import render_to_string
from .models import Column, Course, Chapter
import markdown
from qaschool.settings import *

columns = Column.objects.filter(visible=True).order_by('sn')
courses = Course.objects.filter(visible=True).order_by('sn')


def index(request):
    return render(request, 'course/index.html', {'columns': columns, 'courses': courses})


def column_detail(request, column_slug):
    column = Column.objects.filter(slug=column_slug)
    if column:
        column = column[0]
    cur_courses = Course.objects.filter(column=column, visible=True).order_by('sn')
    return render(request, 'course/column.html', {'column': column, 'cur_courses': cur_courses, 'columns': columns, 'courses': courses})


def course_detail(request, course_slug):
    course = Course.objects.filter(slug=course_slug, visible=True)
    if course:
        course = course[0]
    chapter_one = Chapter.objects.filter(course=course, status='p').order_by('sn').first()

    if chapter_one:
        return chapter_detail(request, course.slug, chapter_one.slug)

    chapters = Chapter.objects.filter(course=course, status='p').order_by('sn')
    return render(request, 'course/course.html', {'course': course, 'chapters': chapters, 'columns': columns, 'courses': courses})


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

    if STATIC_PAGES:
        return render(request, 'course/chapter.html', {'chapter': chapter, 'chapters': chapters, 'columns': columns, 'courses': courses})
    else:
        # 生成静态页面
        static_html = os.path.join(BASE_DIR, 'pages', 'course', '{}.html'.format(chapter.slug))

        if not os.path.exists(static_html):
            tpl = os.path.join(TEMPLATES[0]['DIRS'][0], 'course', 'chapter.html')
            content = render_to_string(tpl, {'chapter': chapter, 'chapters': chapters, 'columns': columns, 'courses': courses})
            with open(static_html, 'w', encoding='utf-8') as static_file:
                static_file.write(content)
        return render(request, static_html)
