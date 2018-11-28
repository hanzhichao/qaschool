from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField('分类名称', max_length=200)
    slug = models.CharField('分类网址', max_length=200, db_index=True, unique=True)
    sn = models.IntegerField("排序", null=True)
    intro = models.CharField('分类简介', max_length=100)
    visible = models.BooleanField("显示", default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))


class Content(models.Model):
    STATUS_CHOICES = (
        ('d', "草稿"),
        ('p', '发布'),
    )

    title = models.CharField('标题', max_length=200)
    keywords = models.CharField('关键字', max_length=80, blank=True, null=True)
    slug = models.CharField('网址', max_length=200, db_index=True, unique=True)
    pic = models.ImageField('缩略图', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='归属分类', on_delete=models.CASCADE, null=True)
    abstract = models.CharField('摘要', max_length=200, blank=True, null=True)
    content = MDTextField("内容", blank=True, null=True)
    html_content = RichTextField("html内容", blank=True, null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    status = models.CharField("状态", max_length=1, choices=STATUS_CHOICES, default='p')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '详情'
        verbose_name_plural = '详情'
        ordering = ['-last_modified_time']

    def get_absolute_url(self):
        return reverse('content', args=(self.category.slug, self.slug,))