from django.db import models
# from DjangoUeditor.models import UEditorField
from django.urls import reverse
from mdeditor.fields import MDTextField


class Column(models.Model):
    pre_column = models.ForeignKey('self', verbose_name='上级栏目', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField('栏目名称', max_length=256)
    manager = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='负责人', on_delete=models.CASCADE)
    slug = models.CharField('栏目网址', max_length=256, db_index=True, unique=True)
    intro = models.TextField('栏目简介', default='', blank=True, null=True)
    visible = models.BooleanField("显示", default=True)
    show_in_nav = models.BooleanField("导航显示", default=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # thumbnail = models.ImageField('缩略图', blank=True, null=True)

    # keywords = models.CharField('关键字', max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))


class Course(models.Model):
    column = models.ForeignKey(Column, verbose_name='所属栏目', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField('课程名称', max_length=256)
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者', on_delete=models.CASCADE)
    slug = models.CharField('课程网址', max_length=256, db_index=True, unique=True)
    intro = models.TextField('课程简介', default='', blank=True, null=True)
    visible = models.BooleanField("显示", default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # thumbnail = models.ImageField('缩略图', blank=True, null=True)

    # keywords = models.CharField('关键字', max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('course', args=(self.slug,))


class Chapter(models.Model):
    STATUS_CHOICES = (
        ('d', "草稿"),
        ('p', '发布'),
    )

    title = models.CharField('标题', max_length=256)
    # keywords = models.CharField('关键字', max_length=80, blank=True, null=True)
    slug = models.CharField('网址', max_length=256, db_index=True, unique=True)
    sn = models.IntegerField("排序", null=True)
    course = models.ForeignKey(Course, verbose_name='归属课程', on_delete=models.CASCADE, blank=True, null=True)

    # thumbnail = models.ImageField('缩略图', blank=True, null=True)

    abstract = models.TextField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选,若为空将摘取正文的前54个字符",)
    content = MDTextField("内容")

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    visible = models.BooleanField("显示", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
        ordering = ['-last_modified_time']

    def get_absolute_url(self):
        return reverse('chapter', args=(self.course.slug, self.slug,))
