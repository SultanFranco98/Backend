from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['image', 'pub_date']
        read_only_fields = ['pub_date']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['phone', 'address']
        read_only_fields = ['phone', 'address']