from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from courses.models import Page, Social, OrderField



class ItemCategory(Page):
    class Meta:
        verbose_name_plural = verbose_name = '题目分类'

    def get_absolute_url(self):
        return reverse('item_category', args=(self.slug,))


class ItemContent(Page, Social):
    category = models.ForeignKey(ItemCategory, related_name='item_contents',
                               on_delete=models.CASCADE, verbose_name="所属分类")
    order = OrderField(for_fields=['category'], blank=True, verbose_name="排序")
    answer = RichTextField("参考答案", blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '题目'

    def get_absolute_url(self):
        return reverse('item_content', args=(self.category.slug, self.slug,))


    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])