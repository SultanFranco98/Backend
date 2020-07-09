from rest_framework import serializers
from .models import Thread


class ThreadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['first', 'second', 'updated', 'timestamp']


class ThreadDetailSerializer(serializers.ModelSerializer):

    message = serializers.CharField(max_length=255)

    class Meta:
        model = Thread
        fields = ['first', 'second', 'message', 'updated', 'timestamp']
        read_only_fields = ['updated', 'timestamp']
