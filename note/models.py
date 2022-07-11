from email.policy import default
from django.db import models
from django.utils import timezone

class Tags(models.Model):
    name = models.CharField('付箋名', max_length=15)

class Notes(models.Model):
    tag = models.ForeignKey(Tags, verbose_name='付箋', on_delete=models.PROTECT, default=1, blank=True, null=True)
    title = models.CharField('タイトル', max_length=50, default='タイトルなし')
    text = models.TextField('メモ')
    created = models.DateTimeField('作成日', default=timezone.now)