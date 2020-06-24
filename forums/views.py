from rest_framework.viewsets import ModelViewSet
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


class ForumViewSet(ModelViewSet):
    permission_classes = [IsClient | IsAdminUser]
    queryset = Forum.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if  self.action == 'list' or self.action == 'update' or self.action == 'destroy':
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
