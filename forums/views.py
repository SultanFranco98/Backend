from django.shortcuts import get_object_or_404
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser
from users.permissions import IsClient, IsConsultant
from rest_framework.permissions import AllowAny
from agrarie.pagintions import CustomResultsSetPagination
from .serializers import *
from .models import *


class CategoryViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomResultsSetPagination


class SubCategoryViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = CustomResultsSetPagination


class TypesViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    pagination_class = CustomResultsSetPagination


class SubTypesViewSet(ModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = SubTypes.objects.all()
    serializer_class = SubTypesSerializer
    pagination_class = CustomResultsSetPagination


class ForumViewSet(ModelViewSet):
    # permission_classes = [IsClient | IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Forum.objects.all()
    pagination_class = CustomResultsSetPagination
    serializer_class = ForumListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'types', 'subtypes']
    search_fields = ['title']

    def get_queryset(self):
        if self.action == 'list':
            return Forum.objects.annotate(
                comment_count=models.Count('comments')
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        queryset = get_object_or_404(Forum, id=kwargs['pk'])
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Forum, id=kwargs['pk'])
        serializer = self.get_serializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Forum, id=kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'list':
            return ForumListSerializer
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'destroy':
            return ForumDetailSerializer
        elif self.action == 'create':
            return ForumCreateSerializer


class CommentViewSet(ModelViewSet):
    # permission_classes = [IsClient | IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
