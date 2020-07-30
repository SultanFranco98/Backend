from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Forum)
class ForumTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kg')


@register(Comment)
class ForumTranslationOptions(TranslationOptions):
    fields = ('description',)
    required_languages = ('ru', 'kg')
