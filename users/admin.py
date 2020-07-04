from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = "Агро Консультирование"
admin.site.site_title = "Агро Консультирование"
admin.site.index_title = "Агро Консультирование"

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('title',)


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
    list_display = ('user', 'get_consultant', 'short_description')
    fields = ('user', 'get_consultant', 'description', 'comment')
    readonly_fields = ('get_consultant',)

    def get_consultant(self, obj):
        return 'Имя:\t{}\n\n' \
               'Фамилия:\t{}\n\n' \
               'Телефон:\t{}\n\n'.format(obj.user.first_name, obj.user.last_name, obj.user.phone)

    get_consultant.short_description = 'Информация о консультанте'


class UserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'phone', 'is_active', 'is_client', 'is_consultant')
    fieldsets = (
        (None, {'fields': (
            'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_client', 'is_consultant',
            'date_joined')}),
    )
    ordering = ('email',)
    readonly_fields = ['date_joined']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'is_active',
                'is_client', 'is_consultant',
            )}
         ),
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'consultant', 'star']
    fields = ['user', 'get_user', 'consultant', 'get_consultant', 'star']
    readonly_fields = ['get_user', 'get_consultant']

    def get_user(self, obj):
        return 'Имя:\t{}\n\n' \
               'Фамилия:\t{}\n\n' \
               'Телефон:\t{}\n\n'.format(obj.user.first_name, obj.user.last_name, obj.user.phone)

    get_user.short_description = 'Информация о клиенте'

    def get_consultant(self, obj):
        return 'Имя:\t{}\n\n' \
               'Фамилия:\t{}\n\n' \
               'Телефон:\t{}\n\n'.format(obj.consultant.user.first_name, obj.consultant.user.last_name,
                                         obj.consultant.user.phone)

    get_consultant.short_description = 'Информация о консультанте'


class RatingStartAdmin(admin.ModelAdmin):
    list_display = ['id', 'value']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['consultant', 'text', 'name', 'email', ]
    fields = ['consultant', 'get_consultant', 'name', 'email', 'text', ]
    readonly_fields = ['get_consultant']

    def get_consultant(self, obj):
        return 'Имя:\t{}\n\n' \
               'Фамилия:\t{}\n\n' \
               'Телефон:\t{}\n\n'.format(obj.consultant.user.first_name, obj.consultant.user.last_name,
                                         obj.consultant.user.phone)

    get_consultant.short_description = 'Информация о консультанте'


admin.site.register(User, UserAdmin)
admin.site.register(RatingStart, RatingStartAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.unregister(Group)
