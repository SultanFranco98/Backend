from django.urls import path
from .views import *

urlpatterns = [
    path('slider/', SliderViewSet.as_view({'get': 'list'})),
]
