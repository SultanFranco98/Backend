from django.db import models


class Slider(models.Model):
    image = models.ImageField(upload_to='slider-image/', blank=True, null=True, verbose_name='Слайдер')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return '{}'.format(self.image)


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return '{}'.format(self.phone, self.address)
