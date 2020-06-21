from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/edit/<int:pk>/', CategoryViewSet.as_view({'put': 'update'})),
    path('category/delete/<int:pk>/', CategoryViewSet.as_view({'delete': 'destroy'})),
    path('category/create', CategoryViewSet.as_view({'post': 'create'})),
]