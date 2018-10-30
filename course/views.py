from django.shortcuts import render
from .models import Column, Course, Lesson
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
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'course/course.html', {'course': course, 'lessons': lessons})


def lesson_detail(request, lesson_slug):
    lesson = Lesson.objects.filter(slug=lesson_slug)
    if lesson:
        lesson = lesson[0]
    lessons = Lesson.objects.filter(course=lesson.course)

    lesson.content = markdown.markdown(lesson.content, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])
    return render(request, 'course/lesson.html', {'lesson': lesson, 'lessons': lessons})


def lesson_detail2(request, course_slug, lesson_slug):
    course = Course.objects.filter(slug=course_slug)
    if course:
        course = course[0]
    lesson = Lesson.objects.filter(course=course, slug=lesson_slug)
    if lesson:
        lesson = lesson[0]
    lessons = Lesson.objects.filter(course=course)
    lesson.content = markdown.markdown(lesson.content, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc', ])
    return render(request, 'course/lesson.html', {'lesson': lesson, 'lessons': lessons})