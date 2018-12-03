from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Base(models.Model):
    title = models.CharField("标题", max_length=200)
    slug = models.SlugField("链接", max_length=200, unique=True)
    keywords = models.CharField('关键字', max_length=200, blank=True, null=True)
    description = models.TextField('描述', blank=True, null=True)

    order = models.IntegerField("排序", blank=True, null=True)

    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE,
                              verbose_name='拥有者')
    created = models.DateTimeField('创建时间', auto_now=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True


    def __str__(self):
        return self.title


class Status(models.Model):
    STATUS_CHOICES = (
        ('d', "草稿"),
        ('p', '发布'),
        ('e', '删除'),
    )
    status = models.CharField("状态", max_length=1, choices=STATUS_CHOICES, default='p')

    class Meta:
        abstract = True

class Social(models.Model):
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    stars = models.IntegerField("评星", default=3)

    class Meta:
        abstract = True


class Category(Base):
    class Meta:
        verbose_name_plural = verbose_name = '分类'

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))


class Course(Base):
    category = models.ForeignKey(Category, related_name='courses',
                                 on_delete=models.CASCADE, verbose_name="所属分类")
    pic = models.ImageField('缩略图', null=True, blank=True)
    is_suggest = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = verbose_name = '课程'

    def get_absolute_url(self):
        return reverse('course', args=(self.slug,))


class Lesson(Base, Status):
    course = models.ForeignKey(Course, related_name='contents',
                               on_delete=models.CASCADE, verbose_name="所属模块")
    md_content = MDTextField("内容", blank=True, null=True)
    html_content = RichTextField("内容", blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '内容'

    def get_absolute_url(self):
        return reverse('lesson', args=(self.course.slug, self.slug,))