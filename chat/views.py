from django.http import Http404
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from agrarie.pagintions import CustomResultsSetPagination
from .serializers import *
from .models import Thread, ChatMessage


class InboxViewSet(ReadOnlyModelViewSet):
    serializer_class = ThreadListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)


class ThreadViewSet(ModelViewSet):
    serializer_class = ThreadDetailSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomResultsSetPagination
    success_url = './'

    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username = self.kwargs.get("email")
        obj, created = Thread.objects.get_or_new(self.request.user, other_username)
        if obj == None:
            raise Http404
        return obj

    def perform_create(self, serializer):
        thread = self.get_object()
        user = self.request.user
        print(serializer.data)
        message = serializer.data['message']
        print(message)
        ChatMessage.objects.create(user=user, thread=thread, message=message)
