from django.contrib import admin
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    fields = ['title_ru', 'title_kg']
    search_fields = ['title']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['title', 'category']
    fields = ['title_ru', 'title_kg', 'category']
    search_fields = ['title', 'category']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subcategory']
    list_filter = ['title', 'subcategory']
    fields = ['title_ru', 'title_kg', 'subcategory']
    search_fields = ['title', 'subcategory']


class SubTypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    list_filter = ['title', 'type']
    fields = ['title_ru', 'title_kg', 'type']
    search_fields = ['title', 'type']


class CategoryConsultantInline(admin.TabularInline):
    model = CategoryConsultant

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return self.extra
        return 0


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    fields = ['title_ru', 'title_kg', 'description_ru', 'description_kg', 'image', 'icon_image']
    list_filter = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(SubTypes, SubTypesAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
