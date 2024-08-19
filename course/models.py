from django.db import models
# from DjangoUeditor.models import UEditorField
from django.urls import reverse
from mdeditor.fields import MDTextField
from qaschool.settings import MEDIA_URL
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class BaseModel():
    created_time = models.DateTimeField('创建时间', null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True

class ShowOptions():
    visiable = models.BooleanField("是否显示", default=True, null=True)
    login_required = models.BooleanField("登录后显示", null=True)
    show_in_nav = models.BooleanField("显示在导航栏", null=True)
    show_in_sidebar = models.BooleanField("显示在侧边栏", null=True)
    show_in_footer = models.BooleanField("显示在底部", null=True)

    class Meta:
        abstract = True


class PageMeta():
    title = models.CharField("标题", max_length=200, blank=True, null=True)
    keywords = models.CharField('关键字', max_length=80, blank=True, null=True)
    description = models.TextField('描述', blank=True, null=True)

    class Meta:
        abstract = True

class PageStatus():
    STATUS_CHOICES = (
        ('d', "草稿"),
        ('p', '发布'),
        ('e', '过期'),
    )

    status = models.CharField("状态", max_length=1, choices=STATUS_CHOICES, default='p')
    publish = models.DateTimeField("延迟发布")
    expire = models.DateTimeField("过期时间")

    class Meta:
        abstract = True
        
class Page(PageMeta, BaseModel):

    sn = models.IntegerField("排序", null=True)

    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    author = models.ForeignKey('auth.User', verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        abstract = True






















class Column(models.Model):
    # pre_column = models.ForeignKey('self', verbose_name='上级分类', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField('分类名称', max_length=200)
    manager = models.ForeignKey('auth.User', verbose_name='负责人', on_delete=models.CASCADE)
    visible = models.BooleanField("显示", default=True)
    show_in_nav = models.BooleanField("导航显示", default=False)
    slug = models.CharField('分类网址', max_length=200, db_index=True, unique=True)
    sn = models.IntegerField("排序", null=True)
    intro = models.CharField('分类简介', max_length=200, blank=True, null=True)
    created_time = models.DateTimeField('创建时间', null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    keywords = models.CharField('关键字', max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))


class Course(models.Model):
    column = models.ForeignKey(Column, verbose_name='所属分类', on_delete=models.CASCADE)
    name = models.CharField('课程名称', max_length=200)
    author = models.ForeignKey('auth.User', verbose_name='作者', on_delete=models.CASCADE)
    slug = models.CharField('课程网址', max_length=200, db_index=True, unique=True)
    sn = models.IntegerField("排序", null=True)
    intro = models.CharField('课程简介', max_length=100)
    visible = models.BooleanField("显示", default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    pic = models.ImageField('缩略图', null=True, blank=True)
    star = models.IntegerField("评星", default=3)
    star_eval_num = models.IntegerField("评星人数", default=1)

    keywords = models.CharField('关键字', max_length=80, blank=True, null=True)

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

    title = models.CharField('标题', max_length=200)
    tags = TaggableManager()
    keywords = models.CharField('关键字', max_length=80, blank=True, null=True)
    slug = models.CharField('网址', max_length=200, db_index=True, unique=True)
    sn = models.IntegerField("排序", null=True)
    course = models.ForeignKey(Course, verbose_name='归属课程', on_delete=models.CASCADE, null=True)
    abstract = models.CharField('摘要', max_length=200, blank=True, null=True)
    content = MDTextField("内容")
    html_content = UEditorField('html内容', height=300, width=1000,
                                          default=u'', blank=True, imagePath="uploads/images/",
                                          toolbars='besttome', filePath='uploads/files/')
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    status = models.CharField("状态", max_length=1, choices=STATUS_CHOICES, default='p')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
        ordering = ['-last_modified_time']

    def get_absolute_url(self):
        return reverse('chapter', args=(self.course.slug, self.slug,))



class Comment(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name="所属章节", related_name='comments', on_delete=models.CASCADE)
    name = models.CharField("姓名", max_length=80, null=True)
    email = models.EmailField("邮件", null=True)
    content = models.TextField("评论内容", null=True)
    visible = models.BooleanField("显示", default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ('created_time',)

    def __str__(self):
        return '{}上{}的评论'.format(self.name, self.chapter)


class Config(models.Model):
    TEMPLATE_CHOICES = (
        ('bootstrap', "bootstrap"),
        ('bootswatch', 'bootswatch'),
    )
    THEME_CHOICES = (
        ('bootstrap', "bootstrap"),
        ('litera', 'litera'),
        ('litera', 'litera'),
        ('materia', 'materia'),
        ('stadstone', 'stadstone'),
        ('yeti', 'yeti'),
    )
    name = models.CharField("名称", max_length=20)
    template = models.CharField("模板", max_length=20, choices=TEMPLATE_CHOICES)

    theme = models.CharField("模板", max_length=20, choices=THEME_CHOICES)
    gen_static_pages = models.BooleanField("是否生成静态页面", default=False)

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置'

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    org = models.CharField('Organization', max_length=128, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()