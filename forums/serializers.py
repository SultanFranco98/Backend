from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'


class SubTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTypes
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'forum', 'description', 'pub_date']
        read_only_fields = ['user', 'pub_date']


class ForumDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'description', 'pub_date',
                  'comments']


class ForumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'description', 'pub_date']
        read_only_fields = ['user', 'pub_date']


class ForumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'user', 'category', 'subcategory', 'types', 'subtypes', 'title', 'description', 'pub_date']
        read_only_fields = ['user', 'pub_date']