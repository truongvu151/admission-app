from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, parsers, status
from rest_framework.decorators import action
from rest_framework.views import Response
from .paginators import AdmissionsDetailsPaginator
from .models import Admission, AdmissionType, Banner, Faculty
from .serializers import (
   AdmissionSerializer,
   AdmissionTypeSerializer,
   FacultySerializer,
   BannerSerializer,
)


# Create your views here.
class AdmissionTypeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = AdmissionType.objects.all()
    serializer_class = AdmissionTypeSerializer
    
    
    @action(methods=['get'], detail=True, url_path='admissions')
    def admissions(self, request, pk):
        admission_type = self.get_object()
        admissions = admission_type.admissions.filter(active=True).order_by('-created_date')[:5]

        kw = request.query_params.get('kw')
        if kw:
            admissions = admissions.filter(title__icontains=kw)

        return Response(AdmissionSerializer(admissions, many=True).data)
    
class AdmissionViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Admission.objects.filter(active=True)
    serializer_class = AdmissionSerializer 
    pagination_class = AdmissionsDetailsPaginator
    
    def get_queryset(self):
        q = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            q = q.filter(subject__icontains=kw)

        ad_type_id = self.request.query_params.get('admission_type_id')
        if ad_type_id:
            q = q.filter(admission_type_id=ad_type_id)

        return q

class FacultyViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
        
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    
class BannerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer