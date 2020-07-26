from django.db import models
from django.contrib.auth import settings
from users.models import User
from forums.models import Category, SubCategory, Types, SubTypes
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категория'))
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_('Подкатегория'), blank=True,
                                    null=True)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name=_('Вид'), blank=True, null=True)
    subtypes = models.ForeignKey(SubTypes, on_delete=models.CASCADE, verbose_name=_('Подвид'), blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    text = models.TextField(verbose_name=_('Текст'))
    pub_date = models.DateField(auto_now_add=True, verbose_name=_('Дата публикации'))
    status = models.BooleanField(default=False, verbose_name=_('Статус'))
    votes = models.IntegerField(blank=True, null=True, verbose_name=_('Оценка'))

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def __str__(self):
        return self.title

    def total_votes(self):
        votes = Vote.objects.filter(article=self.pk, vote=True, article__status=True).count()
        self.votes = votes
        self.save()
        return self.votes


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    vote = models.BooleanField(verbose_name='Оценка')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=_('Статья'))
    pub_date = models.DateField(auto_now_add=True, verbose_name=_('Дата публикации'))

    class Meta:
        verbose_name = _('Оценка')
        verbose_name_plural = _('Оценки')

    def __str__(self):
        return '{}'.format(self.user)


class ArticleAddition(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=_('Статья'),
                                related_name='additions')
    subtitle = models.CharField(max_length=100, verbose_name=_('Подзаголовок'))
    subtext = models.TextField(verbose_name='Подтекст')

    class Meta:
        verbose_name = _('Раздел в статье')
        verbose_name_plural = _('Разделы в статье')

    def __str__(self):
        return self.subtitle
