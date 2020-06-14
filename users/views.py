from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import *


class RegistrationClientViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationClientSerializer


class RegistrationConsultantViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationConsultantSerializer


class RatingViewSet(ModelViewSet):
    serializer_class = RatingCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ConsultantViewSet(ReadOnlyModelViewSet):
    queryset = Consultant.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ConsultantListSerializer
        elif self.action == 'retrieve':
            return ConsultantDetailSerializer


class CategoryConsultantViewSet(ReadOnlyModelViewSet):
    queryset = CategoryConsultant.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryConsultantListSerializer
        elif self.action == 'retrieve':
            return CategoryConsultantDetailSerializer


class ImageConsultantViewSet(ReadOnlyModelViewSet):
    queryset = ImageConsultant.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ImageConsultantListSerializer
        elif self.action == 'retrieve':
            return ImageConsultantDetailSerializer
