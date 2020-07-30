from rest_framework import serializers
from .models import *
from users.serializers import UsersListSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UsersListSerializer(read_only=True, many=False)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'forum', 'description', 'pub_date']
        read_only_fields = ['user', 'pub_date']


class ForumDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'pub_date',
                  'comments']
        read_only_fields = ['user', 'pub_date']


class ForumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'pub_date']
        read_only_fields = ['user', 'pub_date']


class ForumListSerializer(serializers.ModelSerializer):
    user = UsersListSerializer(many=False, read_only=True)
    comment_count = serializers.IntegerField()

    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'pub_date', 'comment_count']
        read_only_fields = ['user', 'pub_date']


class ForumSearchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'pub_date']
