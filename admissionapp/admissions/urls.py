from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register('admissiontypes', views.AdmissionTypeViewSet, basename='type')


urlpatterns = [
    path('', include(r.urls)),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)