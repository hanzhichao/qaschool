from django.shortcuts import render
from .models import Column, Course, Chapter
import markdown


def index(request):
    columns = Column.objects.all()
    courses = Course.objects.all()
    # return HttpResponse(settings.STATIC_ROOT)
    return render(request, 'course/index.html', {'columns': columns, 'courses': courses})


def column_detail(request, column_slug):
    # return HttpResponse('column slug: ' + column_slug)
    column = Column.objects.filter(slug=column_slug)
    if column:
        column = column[0]
    columns = Column.objects.all()
    courses = Course.objects.filter(column=column)
    # return render(request, 'course/column.html', {'column': column, 'courses': courses, 'columns': columns})
    return render(request, 'course/column.html', {'column': column, 'courses': courses, 'columns': columns})


def course_detail(request, course_slug):
    # return HttpResponse('column slug: ' + column_slug)
    course = Course.objects.filter(slug=course_slug)
    if course:
        course = course[0]
    chapters = Chapter.objects.filter(course=course)
    return render(request, 'course/course.html', {'course': course, 'chapters': chapters})


def chapter_detail(request, chapter_slug):
    chapter = Chapter.objects.filter(slug=chapter_slug)
    if chapter:
        chapter = chapter[0]
    chapters = Chapter.objects.filter(course=chapter.course)

    # 浏览量 + 1
    chapter.views += 1

    chapter.content = markdown.markdown(chapter.content, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])
    return render(request, 'course/chapter.html', {'chapter': chapter, 'chapters': chapters})


def chapter_detail2(request, course_slug, chapter_slug):
    course = Course.objects.filter(slug=course_slug)
    if course:
        course = course[0]
    chapter = Chapter.objects.filter(course=course, slug=chapter_slug)
    if chapter:
        chapter = chapter[0]

    # 浏览量 + 1
    chapter.views += 1
    chapter.save()
    chapters = Chapter.objects.filter(course=course)
    chapter.content = markdown.markdown(chapter.content, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])
    return render(request, 'course/chapter.html', {'chapter': chapter, 'chapters': chapters})