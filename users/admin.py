from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(RatingStart)
admin.site.register(Rating)
admin.site.register(Consultant)
admin.site.register(Category)
admin.site.register(ImageConsultant)
admin.site.register(CategoryConsultant)
