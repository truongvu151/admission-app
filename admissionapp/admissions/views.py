from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, parsers, status
from rest_framework.decorators import action
from rest_framework.views import Response
from .models import AdmissionType
from .serializers import (
   AdmissionTypeSerializer,
)


# Create your views here.
class AdmissionTypeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = AdmissionType.objects.all()
    serializer_class = AdmissionTypeSerializer
    

class AdmissionViewSet(viewsets.ViewSet):
    
    