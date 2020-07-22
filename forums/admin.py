from django.contrib import admin
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'description', 'pub_date']
    readonly_fields = ['pub_date']

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return self.extra
        return 0


class ForumAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['user', 'title', 'pub_date']
    list_filter = ['user__email', 'user__first_name', 'user__last_name']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['pub_date']
    ordering = ['-pub_date']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['title', 'category']
    search_fields = ['title', 'category']


class TypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subcategory']
    list_filter = ['title', 'subcategory']
    search_fields = ['title', 'subcategory']


class SubTypesAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    list_filter = ['title', 'type']
    search_fields = ['title', 'type']


admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(SubTypes, SubTypesAdmin)
admin.site.register(Forum, ForumAdmin)
