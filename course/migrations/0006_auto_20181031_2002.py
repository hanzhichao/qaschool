# Generated by Django 2.1 on 2018-10-31 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20181031_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='sn',
            field=models.IntegerField(null=True, verbose_name='排序'),
        ),
        migrations.AddField(
            model_name='course',
            name='sn',
            field=models.IntegerField(null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='status',
            field=models.CharField(choices=[('d', '草稿'), ('p', '发布')], max_length=1, verbose_name='状态'),
        ),
    ]
