# Generated by Django 2.1 on 2018-12-03 12:29

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20181203_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='链接')),
                ('keywords', models.CharField(blank=True, max_length=200, null=True, verbose_name='关键字')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '发布'), ('e', '删除')], default='p', max_length=1, verbose_name='状态')),
                ('md_content', mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='内容')),
                ('html_content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='内容')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.Course', verbose_name='所属模块')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_related', to=settings.AUTH_USER_MODEL, verbose_name='拥有者')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容',
            },
        ),
        migrations.RemoveField(
            model_name='content',
            name='course',
        ),
        migrations.RemoveField(
            model_name='content',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
