from django.contrib import admin
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'description', 'pub_date']
    readonly_fields = ['pub_date']


class ForumAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['user', 'title', 'description', 'pub_date']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subcategory']


class SubTypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']


admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(SubTypes, SubTypesAdmin)
admin.site.register(Forum, ForumAdmin)


