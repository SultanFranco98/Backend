from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['image', 'pub_date']
        read_only_fields = ['pub_date']
