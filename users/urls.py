from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/client', RegistrationClientViewSet.as_view({'post': 'create'})),
    path('signup/consultant', RegistrationConsultantViewSet.as_view({'post': 'create'})),

    path('profile/', UserViewSet.as_view({'get': 'list'})),

    path('consultants/', ConsultantViewSet.as_view({'get': 'list'})),
    path('consultants/<int:pk>/', ConsultantViewSet.as_view({'get': 'retrieve'})),

    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/edit/<int:pk>/', CategoryViewSet.as_view({'put': 'update'})),
    path('category/delete/<int:pk>/', CategoryViewSet.as_view({'delete': 'destroy'})),
    path('category/create', CategoryViewSet.as_view({'post': 'create'})),

    path('specialty/', SpecialtyViewSet.as_view({'get': 'list'})),
    path('specialty/<int:pk>/', SpecialtyViewSet.as_view({'get': 'retrieve'})),
    path('specialty/edit/<int:pk>/', SpecialtyViewSet.as_view({'put': 'update'})),
    path('specialty/delete/<int:pk>/', SpecialtyViewSet.as_view({'delete': 'destroy'})),
    path('specialty/create', SpecialtyViewSet.as_view({'post': 'create'})),


    path('rating/', RatingViewSet.as_view({'get': 'list'})),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve'})),
    path('rating/delete/<int:pk>/', RatingViewSet.as_view({'delete': 'destroy'})),
    path('rating/create', RatingViewSet.as_view({'post': 'create'})),

    path('reviews/', ReviewsViewSet.as_view({'get': 'list'})),
    path('reviews/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve'})),
    path('reviews/edit/<int:pk>/', ReviewsViewSet.as_view({'put': 'update'})),
    path('reviews/delete/<int:pk>/', ReviewsViewSet.as_view({'delete': 'destroy'})),
    path('reviews/create/', ReviewsViewSet.as_view({'post': 'create'})),

    path('rating-star/', RatingStarViewSet.as_view({'get': 'list'})),
    path('rating-star/<int:pk>/', RatingStarViewSet.as_view({'get': 'retrieve'})),
    path('rating-star/edit/<int:pk>/', RatingStarViewSet.as_view({'put': 'update'})),
    path('rating-star/delete/<int:pk>/', RatingStarViewSet.as_view({'delete': 'destroy'})),
    path('rating-star/create', RatingStarViewSet.as_view({'post': 'create'})),

    path('category-consultants/', CategoryConsultantViewSet.as_view({'get': 'list'})),
    path('category-consultants/<int:pk>/', CategoryConsultantViewSet.as_view({'get': 'retrieve'})),
    path('category-consultants/edit/<int:pk>/', CategoryConsultantViewSet.as_view({'put': 'update'})),
    path('category-consultants/delete/<int:pk>/', CategoryConsultantViewSet.as_view({'delete': 'destroy'})),

    path('certificate-consultant/', ImageConsultantViewSet.as_view({'get': 'list'})),
    path('certificate-consultant/<int:pk>', ImageConsultantViewSet.as_view({'get': 'retrieve'})),
    path('certificate-consultant/edit/<int:pk>', ImageConsultantViewSet.as_view({'put': 'update'})),
    path('certificate-consultant/delete/<int:pk>', ImageConsultantViewSet.as_view({'delete': 'destroy'})),

]
