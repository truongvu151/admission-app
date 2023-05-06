from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, parsers, status
from rest_framework.decorators import action
from rest_framework.views import Response

from .permissions import CommentOwner
from .paginators import AdmissionsDetailsPaginator, FAQPaginator
from .models import FAQ, Admission, AdmissionType, Banner, Comment, Faculty, ReplyComment, UserAccount
from .serializers import (
   AdmissionSerializer,
   AdmissionTypeSerializer,
   CommentSerializer,
   FAQSerializer,
   FacultySerializer,
   BannerSerializer,
   ReplyCommentSerializer,
   UserAccountSerializer,
)


# Create your views here.
# This is a Python class that defines a ViewSet and a ListAPIView for AdmissionType objects, with a
# nested action method to retrieve related Admission objects filtered by a keyword.
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
    
    def get_permissions(self):
        if self.action in ['comments']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    
    @action(methods=['GET', 'POST'], detail=True, url_path='comments')
    def comments(self, request, pk):
        c = Comment(content = request.data['content'], 
                    admission = self.get_object(), 
                    user = request.user)
        c.save()

        return Response(CommentSerializer(c).data, status=status.HTTP_201_CREATED)

class FacultyViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    
class BannerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = UserAccount.objects.filter(is_active=True)
    serializer_class = UserAccountSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['current_user']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get', 'put'], detail=False, url_path='current-user')
    def current_user(self, request):
        u = request.user
        if request.method.__eq__('PUT'):
            for k, v in request.data.items():
                setattr(u, k, v)
            u.save()

        return Response(UserAccountSerializer(u, context={'request': request}).data)

class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer
    permission_classes = [CommentOwner, ]
    
    @action(methods=['POST'], detail=True, url_path='replies')
    def replies(self, request, pk):
        if permissions.IsAdminUser:
            rep = ReplyComment(content = request.data['content'], 
                        comment = self.get_object(), 
                        user = request.user)
            rep.save()
        else:
            raise permissions.PermissionDenied()

        return Response(ReplyCommentSerializer(rep).data, status=status.HTTP_201_CREATED)
    
class FAQViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    pagination_class = FAQPaginator
