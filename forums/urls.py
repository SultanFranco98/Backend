from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('categories/edit/<int:pk>/', CategoryViewSet.as_view({'put': 'update'})),
    path('categories/delete/<int:pk>/', CategoryViewSet.as_view({'delete': 'destroy'})),
    path('categories/create', CategoryViewSet.as_view({'post': 'create'})),

    path('forums/', ForumViewSet.as_view({'get': 'list'})),
    path('forums/<int:pk>', ForumViewSet.as_view({'get': 'retrieve'})),
    path('forums/edit/<int:pk>', ForumViewSet.as_view({'put': 'update'})),
    path('forums/delete/<int:pk>', ForumViewSet.as_view({'delete': 'destroy'})),
    path('forums/create', ForumViewSet.as_view({'post': 'create'})),

    path('comments/', CommentViewSet.as_view({'get': 'list'})),
    path('comments/<int:pk>', CommentViewSet.as_view({'get': 'retrieve'})),
    path('comments/edit/<int:pk>', CommentViewSet.as_view({'put': 'update'})),
    path('comments/delete/<int:pk>', CommentViewSet.as_view({'delete': 'destroy'})),
    path('comments/create', CommentViewSet.as_view({'post': 'create'})),
]
