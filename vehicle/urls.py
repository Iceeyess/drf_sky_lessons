from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from vehicle import views

app_name = VehicleConfig.name


router = DefaultRouter()
router.register(r'cars', views.CarViewSet, basename='cars')

urlpatterns = [
    path('moto/create/', views.MotoCreateAPIView.as_view(), name='moto-create'),
    path('moto/', views.MotoListAPIView.as_view(), name='moto-list'),
    path('moto/<int:pk>/', views.MotoRetrieveAPIView.as_view(), name='moto-get'),
    path('moto/update/<int:pk>/', views.MotoUpdateAPIView.as_view(), name='moto-update'),
    path('moto/delete/<int:pk>/', views.MotoDeleteAPIView.as_view(), name='moto-delete'),


] + router.urls
