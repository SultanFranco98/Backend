from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .models import Slider
from .serializers import *


class SliderViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsClient | IsConsultant | IsAdminUser]
    permission_classes = [AllowAny]
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ContactInfoViewSet(ReadOnlyModelViewSet):
    # permission_classes = [IsClient | IsConsultant | IsAdminUser]
    permission_classes = [AllowAny]
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
