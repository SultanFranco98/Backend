from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import filters
from article.models import Article
from users.models import Consultant
from forums.models import Forum
from forums.serializers import ForumSearchListSerializer
from users.serializers import ConsultantSearchListSerializer
from article.serializers import ArticleListSerializer


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10


class GlobalSearchAPIView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination

    querylist = [
        {'queryset': Article.objects.filter(status=True), 'serializer_class': ArticleListSerializer},
        {'queryset': Consultant.objects.filter(user__is_active=True),
         'serializer_class': ConsultantSearchListSerializer},
        {'queryset': Forum.objects.all(), 'serializer_class': ForumSearchListSerializer},
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'title',]