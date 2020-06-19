from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
    fields = ('user', 'get_consultant', 'description', 'comment')
    readonly_fields = ('get_consultant', 'description', 'comment')

    def get_consultant(self, obj):
        return 'Имя:\t{}\n\n' \
               'Фамилия:\t{}\n\n' \
               'email:\t{}\n\n' \
               'Телефон:\t{}\n\n'.format(obj.user.first_name, obj.user.last_name, obj.user.email,
                                         obj.user.phone)

    get_consultant.short_description = 'Информация о консультанте'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_client', 'is_consultant')
    fieldsets = (
        (None, {'fields': (
            'username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_client', 'is_consultant',
            'date_joined')}),
    )
    search_fields = ('username',)
    readonly_fields = ['date_joined']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'is_active',
                'is_client', 'is_consultant',
            )}
         ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(RatingStart)
admin.site.register(Rating)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Category)
admin.site.register(Specialty)
