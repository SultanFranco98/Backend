from django.db import models


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
