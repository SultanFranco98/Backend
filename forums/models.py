from django.db import models
from django.contrib.auth import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Категория'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='category-image/', blank=True, null=True, verbose_name=_('Фотография'))
    icon_image = models.ImageField(upload_to='category-icon/', blank=True, null=True, verbose_name=_('Иконка'))

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Подкатегория'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категория'))

    class Meta:
        verbose_name = _('Подкатегория')
        verbose_name_plural = _('Подкатегории')

    def __str__(self):
        return self.title


class Types(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Виды'))
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_('Подкатегория'))

    class Meta:
        verbose_name = _('Вид')
        verbose_name_plural = _('Виды')

    def __str__(self):
        return self.title


class SubTypes(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Подвиды'))
    type = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name=_('Вид'))

    class Meta:
        verbose_name = _('Подвид')
        verbose_name_plural = _('Подвиды')

    def __str__(self):
        return self.title


class Forum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категории'))
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_('Подкатегории'), blank=True, null=True)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name=_('Виды'), blank=True, null=True)
    subtypes = models.ForeignKey(SubTypes, on_delete=models.CASCADE, verbose_name=_('Подвиды'), blank=True, null=True)
    title = models.TextField(max_length=5000, verbose_name=_('Вопрос'))
    pub_date = models.DateField(auto_now_add=True, verbose_name=_('Дата публикации'))

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Форум'))
    description = models.TextField(max_length=5000, verbose_name=_('Комментарии'))
    pub_date = models.DateField(auto_now_add=True, verbose_name=_('Дата публикации'))

    class Meta:
        verbose_name = _('Комментарии')
        verbose_name_plural = _('Комментарии')

    def __str__(self):
        return '{}'.format(self.user)



