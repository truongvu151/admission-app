from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register('users', views.UserViewSet, basename='user')
r.register('admission-types', views.AdmissionTypeViewSet, basename='type')
r.register('admissions', views.AdmissionViewSet, basename='admission')
r.register('faculties', views.FacultyViewSet, basename='faculty')
r.register('banners', views.BannerViewSet, basename='banner')

urlpatterns = [
    path('', include(r.urls)),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)