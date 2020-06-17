from django.contrib import admin

from .models import *


class CategoryConsultantInline(admin.TabularInline):
    model = CategoryConsultant


class ImageConsultantAdmin(admin.ModelAdmin):
    fields = ('certificate_tag',)
    readonly_fields = ('certificate_tag',)


class ImageConsultantInline(admin.TabularInline):
    model = ImageConsultant
    fields = ('certificate_tag', 'certificate_image')
    readonly_fields = ('certificate_tag',)


class ConsultantAdmin(admin.ModelAdmin):
    inlines = (CategoryConsultantInline, ImageConsultantInline)
    fields = ('get_consultant', 'description', 'comment')
    readonly_fields = ('get_consultant', 'description', 'comment')

    def get_consultant(self, obj):
        return 'Логин:\t{}\n\n' \
               'Имя:\t{}\n\n' \
               'Фамилия:\t{}\n\n' \
               'email:\t{}\n\n' \
               'Телефон:\t{}\n\n'.format(obj.user.username, obj.user.first_name, obj.user.last_name, obj.user.email,
                                         obj.user.phone)

    get_consultant.short_description = 'Информация о консультанте'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User)
admin.site.register(RatingStart)
admin.site.register(Rating)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Category)
