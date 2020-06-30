from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser
from users.permissions import IsClient, IsConsultant
from .serializers import *
from .models import *


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class TypesViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Types.objects.all()
    serializer_class = TypesSerializer


class SubTypesViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SubTypes.objects.all()
    serializer_class = SubTypesSerializer


class ForumViewSet(ModelViewSet):
    permission_classes = [IsClient | IsAdminUser]
    queryset = Forum.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'update' or self.action == 'destroy':
            return ForumListSerializer
        elif self.action == 'retrieve':
            return ForumDetailSerializer
        elif self.action == 'create':
            return ForumCreateSerializer


class CommentViewSet(ModelViewSet):
    permission_classes = [IsClient | IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubCategoriesByCategoriesViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsClient | IsConsultant | IsAdminUser]
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = SubCategory.objects.filter(category_id=self.kwargs["pk"])
        return queryset


class TypesBySubCategoriesViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsClient | IsConsultant | IsAdminUser]
    serializer_class = TypesSerializer

    def get_queryset(self):
        queryset = Types.objects.filter(subcategory_id=self.kwargs["pk"])
        return queryset


class SubTypesByTypesViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsClient | IsConsultant | IsAdminUser]
    serializer_class = SubTypesSerializer

    def get_queryset(self):
        queryset = SubTypes.objects.filter(type_id=self.kwargs["pk"])
        return queryset
