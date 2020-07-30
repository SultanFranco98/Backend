from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kg')


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kg')


@register(Types)
class TypesTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kg')


@register(SubTypes)
class SubTypesTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kg')


@register(Specialty)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', 'kg')
