from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from courses.models import Page, Social, OrderField



class ResCategory(Page):
    class Meta:
        verbose_name_plural = verbose_name = '资源分类'

    def get_absolute_url(self):
        return reverse('res_category', args=(self.slug,))


class ResContent(Page, Social):
    category = models.ForeignKey(ResCategory, related_name='res_contents',
                               on_delete=models.CASCADE, verbose_name="所属分类")
    pic = models.ImageField('缩略图', null=True, blank=True)
    models.ImageField('缩略图', null=True, blank=True)
    order = OrderField(for_fields=['category'], blank=True, verbose_name="排序")
    html_content = RichTextField("内容", blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '资源内容'

    def get_absolute_url(self):
        return reverse('res_content', args=(self.category.slug, self.slug,))


    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])