from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'votes', 'category', 'subcategory', 'user']


class VoteAdmin(admin.ModelAdmin):
    list_display = ['article', 'vote', 'user']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Vote, VoteAdmin)
