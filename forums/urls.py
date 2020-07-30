from django.urls import path
from .views import *

urlpatterns = [
    path('forums/', ForumViewSet.as_view({'get': 'list'})),
    path('forums/<int:pk>', ForumViewSet.as_view({'get': 'retrieve'})),
    path('forums/edit/<int:pk>', ForumViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('forums/delete/<int:pk>', ForumViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('forums/create', ForumViewSet.as_view({'post': 'create'})),

    path('comments/', CommentViewSet.as_view({'get': 'list'})),
    path('comments/<int:pk>', CommentViewSet.as_view({'get': 'retrieve'})),
    path('comments/edit/<int:pk>', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('comments/delete/<int:pk>', CommentViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('comments/create', CommentViewSet.as_view({'post': 'create'})),
]
