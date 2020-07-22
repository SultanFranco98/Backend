from django.db import models
from django.contrib.auth import settings
from users.models import User
from forums.models import Category, SubCategory, Types, SubTypes


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория', blank=True,
                                    null=True)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name='Вид', blank=True, null=True)
    subtypes = models.ForeignKey(SubTypes, on_delete=models.CASCADE, verbose_name='Подвид', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    status = models.BooleanField(default=False, verbose_name='Статус')
    votes = models.IntegerField(blank=True, null=True, verbose_name='Оценка')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def total_votes(self):
        votes = Vote.objects.filter(article=self.pk, vote=True, article__status=True).count()
        self.votes = votes
        self.save()
        return self.votes


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    vote = models.BooleanField(verbose_name='Оценка')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return '{}'.format(self.user)


class ArticleAddition(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья',
                                related_name='additions')
    subtitle = models.CharField(max_length=100, verbose_name='Подзаголовок')
    subtext = models.TextField(verbose_name='Подтекст')

    class Meta:
        verbose_name = 'Раздел в статье'
        verbose_name_plural = 'Разделы в статье'

    def __str__(self):
        return self.subtitle
