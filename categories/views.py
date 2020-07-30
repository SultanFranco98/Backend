from .models import *
from agrarie.pagintions import CustomResultsSetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from users.permissions import IsClient, IsConsultant
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import *


class CategoryViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomResultsSetPagination


class SubCategoryViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = CustomResultsSetPagination


class TypesViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    pagination_class = CustomResultsSetPagination


class SubTypesViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = SubTypes.objects.all()
    serializer_class = SubTypesSerializer
    pagination_class = CustomResultsSetPagination


class SpecialtyViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    pagination_class = CustomResultsSetPagination