from django.db import models
from django.contrib.auth import settings


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title


class Types(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Виды')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'

    def __str__(self):
        return self.title


class Forum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегории')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments', verbose_name='Форум')
    description = models.TextField(max_length=5000, verbose_name='Комментарии')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '{}'.format(self.user)
