from rest_framework import serializers
from .models import Thread, ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'


class ThreadListSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True)

    class Meta:
        model = Thread
        fields = ['id', 'first', 'second', 'updated', 'timestamp', 'messages']
        read_only_fields = ['messages']


class ThreadDetailSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=255)

    class Meta:
        model = Thread
        fields = ['first', 'second', 'message', 'updated', 'timestamp']
        read_only_fields = ['updated', 'timestamp']
