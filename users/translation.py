from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Consultant)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'comment')
    required_languages = ('ru', 'kg')


@register(Specialty)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kg')


@register(Reviews)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('ru', 'kg')