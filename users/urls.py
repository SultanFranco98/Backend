from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', CustomTokenView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('signup/client', RegistrationClientViewSet.as_view({'post': 'create'})),
    path('signup/consultant', RegistrationConsultantViewSet.as_view({'post': 'create'})),

    path('profile/', UserViewSet.as_view({'get': 'list'})),
    path('profile/edit/<str:name>/', UserViewSet.as_view({'get': 'retrieve','put': 'update'})),
    path('profile/photo/edit/<str:name>/', ProfilePhotoViewSet.as_view({'get': 'retrieve','put': 'update'})),

    path('consultants/certificate/create', CertificateViewSet.as_view({'post': 'create'})),
    path('consultants/<int:pk>/', ConsultantViewSet.as_view({'get': 'retrieve'})),
    path('specialty/<int:pk>/consultants/', ConsultantViewSet.as_view({'get': 'list'})),

    path('specialty/', SpecialtyViewSet.as_view({'get': 'list'})),
    path('specialty/create', SpecialtyViewSet.as_view({'post': 'create'})),


    path('ratings/', RatingViewSet.as_view({'get': 'list'})),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve'})),
    path('ratings/delete/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('ratings/create', RatingViewSet.as_view({'post': 'create'})),

    path('reviews/', ReviewsViewSet.as_view({'get': 'list'})),
    path('reviews/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve'})),
    path('reviews/edit/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('reviews/delete/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('reviews/create/', ReviewsViewSet.as_view({'post': 'create'})),
]
