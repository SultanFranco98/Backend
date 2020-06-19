from django.db.models.functions import Concat
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import *
from django.db.models import Avg
from .permissions import IsClient, IsConsultant


class RegistrationClientViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationClientSerializer


class RegistrationConsultantViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Consultant.objects.all()
    serializer_class = RegistrationConsultantSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    permission_classes = [IsClient | IsAdminUser]
    serializer_class = RatingListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ConsultantViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsClient | IsConsultant | IsAdminUser]

    def get_queryset(self):
        consultant = Consultant.objects.filter(user__is_active=False).annotate(
            middle_star=(Avg("ratings__star")),
        )
        return consultant

    def get_serializer_class(self):
        if self.action == 'list':
            return ConsultantListSerializer
        elif self.action == 'retrieve':
            return ConsultantDetailSerializer


class CategoryConsultantViewSet(ModelViewSet):
    queryset = CategoryConsultant.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryConsultantListSerializer
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'destroy':
            return CategoryConsultantDetailSerializer


class ImageConsultantViewSet(ModelViewSet):
    queryset = ImageConsultant.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'list':
            return ImageConsultantListSerializer
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'destroy':
            return ImageConsultantDetailSerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SpecialtyViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class RatingStarViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = RatingStart.objects.all()
    serializer_class = RatingStarSerializer


class ReviewsViewSet(ModelViewSet):
    permission_classes = [IsClient | IsAdminUser]
    queryset = Reviews.objects.all()

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.pk)
        serializer.save(name='{} {}'.format(user.first_name, user.last_name), email=user.email)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'destroy' or self.action == 'update':
            return ReviewsListSerializer
        elif self.action == 'retrieve' or self.action == 'list':
            return ReviewsDetailSerializer


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsClient | IsConsultant | IsAdminUser]
    serializer_class = UsersDetailSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.pk)
