# Generated by Django 2.1 on 2018-10-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20181031_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='pre_column',
        ),
        migrations.AddField(
            model_name='chapter',
            name='keywords',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='关键字'),
        ),
        migrations.AddField(
            model_name='column',
            name='keywords',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='关键字'),
        ),
        migrations.AddField(
            model_name='course',
            name='keywords',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='关键字'),
        ),
    ]
