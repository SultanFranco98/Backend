from django.urls import path, re_path

from .views import ThreadViewSet, InboxViewSet

app_name = 'chat'
urlpatterns = [
    path("", InboxViewSet.as_view({'get': 'list'})),
    re_path(r"^(?P<email>[\w.@+-]+)", ThreadViewSet.as_view({'post': 'create'})),
]