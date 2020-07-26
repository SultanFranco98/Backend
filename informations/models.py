from django.db import models
from django.utils.translation import gettext_lazy as _


class Slider(models.Model):
    image = models.ImageField(upload_to='slider-image/', blank=True, null=True, verbose_name=_('Слайдер'))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата'))

    class Meta:
        verbose_name = _('Слайдер')
        verbose_name_plural = _('Слайдеры')

    def __str__(self):
        return '{}'.format(self.image)


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, verbose_name=_('Номер телефона'))
    address = models.CharField(max_length=250, verbose_name=_('Адрес'))

    class Meta:
        verbose_name = _('Контактная информация')
        verbose_name_plural = _('Контактная информация')

    def __str__(self):
        return '{}'.format(self.phone, self.address)
