from django.db import models
from django.urls import reverse
from django.utils import timezone

class Words(models.Model):
    spell = models.CharField('単語', max_length=30, unique=True)
    ts = models.CharField('訳', max_length=50)
    pt = models.CharField('過去形', blank=True, max_length=30)
    pp = models.CharField('過去分詞', blank=True, max_length=30)
    prp = models.CharField('現在分詞', blank=True, max_length=30)
    example = models.TextField('例文', blank=True)
    created = models.DateTimeField('作成日', default=timezone.now)
    browsed = models.DateTimeField('最終閲覧日', default=timezone.now)
    wverb = models.BooleanField('動詞かどうか', default=True)

    def __str__(self):
        return self.spell

    def get_absolute_url(self):
        return reverse('ew:detail', kwargs={'slug':self.kwargs['slug']})

class Examples(models.Model):
    sentence = models.TextField('文')
    ts = models.TextField('訳', blank=True)
    created = models.DateTimeField('作成日', default=timezone.now)
