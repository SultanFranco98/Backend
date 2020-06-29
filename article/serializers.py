from rest_framework import serializers
from .models import *


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    article = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'user', 'vote', 'article', 'pub_date']
        read_only_fields = ['user', 'pub_date']


class ArticleSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(source='total_votes', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'consultant', 'category', 'subcategory', 'title', 'text', 'pub_date', 'votes']
        read_only_fields = ['consultant', 'pub_date', 'votes']



