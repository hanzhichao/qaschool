# Generated by Django 2.1 on 2018-12-03 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_is_suggest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
