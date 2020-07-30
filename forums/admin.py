from django.contrib import admin
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'description_ru', 'description_kg', 'pub_date']
    readonly_fields = ['pub_date']

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return self.extra
        return 0


class ForumAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['user', 'title', 'pub_date']
    fields = ['user', 'category', 'subcategory', 'types', 'subtypes', 'title_ru', 'title_kg', 'pub_date']
    list_filter = ['user__email', 'user__first_name', 'user__last_name', 'category', 'subcategory', 'types', 'subtypes']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['pub_date']
    ordering = ['-pub_date']


admin.site.register(Forum, ForumAdmin)
