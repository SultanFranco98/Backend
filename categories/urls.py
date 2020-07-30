from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('subcategories/', SubCategoryViewSet.as_view({'get': 'list'})),
    path('subcategories/<int:pk>/', SubCategoryViewSet.as_view({'get': 'retrieve'})),
    path('types/', TypesViewSet.as_view({'get': 'list'})),
    path('types/<int:pk>/', TypesViewSet.as_view({'get': 'retrieve'})),
    path('subtypes/', SubTypesViewSet.as_view({'get': 'list'})),
    path('subtypes/<int:pk>/', SubTypesViewSet.as_view({'get': 'retrieve'})),
    path('specialty/', SpecialtyViewSet.as_view({'get': 'list'})),
    path('specialty/<int:pk>/', SpecialtyViewSet.as_view({'get': 'retrieve'})),
    path('specialty/create', SpecialtyViewSet.as_view({'post': 'create'})),
]
