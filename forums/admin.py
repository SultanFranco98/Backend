from django.contrib import admin
from .models import *


class ForumAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'pub_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'pub_date']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subcategory']


admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Comment)
