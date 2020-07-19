from rest_framework import serializers
from .models import *
from users.serializers import UsersListSerializer


class VoteSerializer(serializers.ModelSerializer):
    user = UsersListSerializer(read_only=True, many=False)
    article = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'user', 'vote', 'article', 'pub_date']
        read_only_fields = ['user', 'pub_date']


class ArticleListSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(source='total_votes', read_only=True)
    user = UsersListSerializer(read_only=True, many=False)

    class Meta:
        model = Article
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'text', 'pub_date', 'status',
                  'votes']
        read_only_fields = ['user', 'pub_date', 'votes', 'status']


class ArticleDetailSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(source='total_votes', read_only=True)
    user = UsersListSerializer(read_only=True, many=False)

    class Meta:
        model = Article
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'text', 'pub_date', 'status',
                  'votes']
        read_only_fields = ['user', 'pub_date', 'votes', 'status']
