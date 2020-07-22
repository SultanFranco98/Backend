from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class InformationsConfig(AppConfig):
    name = 'informations'
    verbose_name = _('Информация на сайте')
