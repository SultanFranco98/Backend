from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/client', RegistrationClientViewSet.as_view({'post': 'create'})),
    path('signup/consultant', RegistrationConsultantViewSet.as_view({'post': 'create'})),

    path('consultants/', ConsultantViewSet.as_view({'get': 'list'})),
    path('consultants/<int:pk>/', ConsultantViewSet.as_view({'get': 'retrieve'})),

    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/create', CategoryViewSet.as_view({'post': 'create'})),

    path('rating/', RatingViewSet.as_view({'get': 'list'})),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve'})),
    path('rating/create', RatingViewSet.as_view({'post': 'create'})),
    path('rating-star/', RatingStarViewSet.as_view({'get': 'list'})),
    path('rating-star/<int:pk>/', RatingStarViewSet.as_view({'get': 'retrieve'})),
    path('rating-star/create', RatingStarViewSet.as_view({'post': 'create'})),

    path('category-consultants/', CategoryConsultantViewSet.as_view({'get': 'list'})),
    path('category-consultants/<int:pk>/', CategoryConsultantViewSet.as_view({'get': 'retrieve'})),

    path('certificate-consultant/', ImageConsultantViewSet.as_view({'get': 'list'})),
    path('certificate-consultant/<int:pk>', ImageConsultantViewSet.as_view({'get': 'retrieve'})),

]
