from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    required_languages = ('ru', 'kg')


@register(ArticleAddition)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('subtitle', 'subtext')
    required_languages = ('ru', 'kg')
