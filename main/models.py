from django.db import models
from django.urls import reverse

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
class ChildSupportInfo(models.Model):
    title = models.CharField("タイトル", max_length=200)
    description = models.TextField("概要", blank=True, null=True)
    content = models.TextField("内容")
    published_date = models.DateTimeField("公開日", auto_now_add=True)

    class Meta:
        verbose_name = "子育て支援情報"
        verbose_name_plural = "子育て支援情報"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 詳細ページ用の URL を返します。urls.py で 'child_support_detail' という名前でパスを定義してください。
        return reverse('child_support_detail', kwargs={'pk': self.pk})