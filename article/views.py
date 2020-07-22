from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from users.permissions import IsClient, IsConsultant
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from agrarie.pagintions import CustomResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters


class VoteViewSet(ModelViewSet):
    # permission_classes = [IsClient | IsConsultant | IsAdminUser]
    permission_classes = [AllowAny]
    serializer_class = VoteSerializer
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        queryset = Vote.objects.filter(article_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        article = Article.objects.get(id=self.kwargs['pk'], status=True)
        return serializer.save(user=self.request.user, article=article)


class ArticleViewSet(ModelViewSet):
    # permission_classes = [IsConsultant | IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    pagination_class = CustomResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'types', 'subtypes']
    search_fields = ['title']

    def get_queryset(self):
        queryset = Article.objects.filter(status=True)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleDetailSerializer
