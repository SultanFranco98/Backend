from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import *
from django.db.models import Avg


class RegistrationClientViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationClientSerializer


class RegistrationConsultantViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationConsultantSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RatingCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ConsultantViewSet(ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        consultant = Consultant.objects.filter(user__is_active=False).annotate(
            middle_star=(Avg("ratings__star"))
        )
        return consultant

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


class CategoryViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RatingStarViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = RatingStart.objects.all()
    serializer_class = RatingStarSerializer
