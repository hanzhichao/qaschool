from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from .fields import OrderField

class VisibleManager(models.Manager):
    def get_queryset(self):
        return super(VisibleManager, self).get_queryset().filter(visible=True).order_by('order')


class Item(models.Model):
    order = models.IntegerField("排序", blank=True, null=True)
    visible = models.BooleanField("显示", default=True)
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE,
                              verbose_name='拥有者')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    objects = VisibleManager()

    class Meta:
        abstract = True

class Page(Item):
    title = models.CharField("标题", max_length=200)
    slug = models.SlugField("链接", max_length=200, unique=True)
    keywords = models.CharField('关键字', max_length=200, blank=True, null=True)
    description = models.TextField('描述', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Social(models.Model):
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)


    class Meta:
        abstract = True


class Category(Page):
    class Meta:
        verbose_name_plural = verbose_name = '教程分类'

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))


class Course(Page):
    category = models.ForeignKey(Category, related_name='courses',
                                 on_delete=models.CASCADE, verbose_name="所属分类")
    order = OrderField(for_fields=['category'], blank=True, verbose_name="排序")
    pic = models.ImageField('缩略图', null=True, blank=True)
    is_suggest = models.BooleanField("推荐课程", default=False)
    stars = models.IntegerField("评星", default=3)

    class Meta:
        verbose_name_plural = verbose_name = '教程'

    def get_absolute_url(self):
        return reverse('course', args=(self.slug,))


class Lesson(Page, Social):
    course = models.ForeignKey(Course, related_name='lessons',
                               on_delete=models.CASCADE, verbose_name="所属课程")
    order = OrderField(for_fields=['course'], blank=True, verbose_name="排序")
    md_content = MDTextField("内容", blank=True, null=True)
    html_content = RichTextField("内容", blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '教程内容'

    def get_absolute_url(self):
        return reverse('lesson', args=(self.course.slug, self.slug,))


    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])


class Poll(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, related_name='polls', on_delete=models.CASCADE, verbose_name="点赞章节")
    created = models.DateTimeField('创建时间', auto_now_add=True)


class Rate(models.Model):
    user = models.ForeignKey(User, related_name='rates', on_delete=models.CASCADE,
                      verbose_name='评星人')
    course = models.ForeignKey(Course, related_name='rates',
                               on_delete=models.CASCADE, verbose_name="所评课程")
    created = models.DateTimeField('创建时间', auto_now_add=True)


class Comment(Item):
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE, verbose_name="所评章节")
    content = models.TextField('评论内容', blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return "{}-{}的评论".format(self.lesson.title, self.owner.username)