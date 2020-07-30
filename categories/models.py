from django.db import models
from users.models import Consultant
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Категория'))

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


class Specialty(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Специальность'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='category-image/', blank=True, null=True, verbose_name=_('Фотография'))
    icon_image = models.ImageField(upload_to='category-icon/', blank=True, null=True, verbose_name=_('Иконка'))

    class Meta:
        verbose_name = _('Специальность')
        verbose_name_plural = _('Специальности')

    def __str__(self):
        return self.title


class CategoryConsultant(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='specialty', verbose_name=_('Консультант'))
    category = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=False, null=False,
                                 verbose_name=_('Специальность'))

    class Meta:
        verbose_name = _('Специальность')
        verbose_name_plural = _('Специальности')

    def __str__(self):
        return '{}'.format(self.consultant)
