from django.contrib import admin

from .models import Thread, ChatMessage

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"


class ChatMessage(admin.TabularInline):
    fields = ['user', 'message', 'timestamp']
    readonly_fields = ['timestamp']
    model = ChatMessage

    def get_extra(self, request, obj=None, **kwargs):
        if obj is None:
            return self.extra
        return 0


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    list_display = ['first', 'second', 'updated']
    fields = ['first', 'second', 'updated']
    readonly_fields = ['updated']


admin.site.register(Thread, ThreadAdmin)
