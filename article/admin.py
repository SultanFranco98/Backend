from django.contrib import admin
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'user', 'votes']
    list_filter = ['user__email', 'user__first_name', 'user__last_name', 'status', 'category', 'subcategory', 'types',
                   'subtypes', 'votes']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['pub_date']
    ordering = ['-pub_date']


class VoteAdmin(admin.ModelAdmin):
    list_display = ['article', 'vote', 'user']
    list_filter = ['user__email', 'user__first_name', 'user__last_name', 'vote']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['pub_date']
    ordering = ['-pub_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Vote, VoteAdmin)
