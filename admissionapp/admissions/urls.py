from django.urls import path, include
from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register('admissiontypes', views.AdmissionTypeViewSet, basename='type')


urlpatterns = [
    path('', include(r.urls)),
]