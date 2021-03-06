from django.contrib import admin
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address']
    list_filter = ['phone', 'address']


admin.site.register(Slider)
admin.site.register(ContactInfo, ContactInfoAdmin)
