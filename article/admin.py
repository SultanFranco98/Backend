from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Агро Консультирование")
admin.site.site_title = _("Агро Консультирование")
admin.site.index_title = _("Агро Консультирование")


class AdditionInline(admin.TabularInline):
    model = ArticleAddition
    fields = ('subtitle_ru', 'subtitle_kg', 'subtext_ru', 'subtext_kg')

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return self.extra
        return 0


class ArticleAdmin(admin.ModelAdmin):
    fields = ['user', 'category', 'subcategory', 'types', 'subtypes', 'title_ru', 'title_kg', 'text_ru', 'text_kg', 'status', 'votes', 'pub_date']
    list_display = ['title', 'status', 'category', 'user', 'votes']
    list_filter = ['user__email', 'user__first_name', 'user__last_name', 'status', 'category', 'subcategory', 'types',
                   'subtypes', 'votes']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['pub_date', 'votes']
    ordering = ['-pub_date']
    inlines = [AdditionInline]


class VoteAdmin(admin.ModelAdmin):
    list_display = ['article', 'vote', 'user']
    list_filter = ['user__email', 'user__first_name', 'user__last_name', 'vote']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['pub_date']
    ordering = ['-pub_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Vote, VoteAdmin)
