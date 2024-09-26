from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import User
from .paginators import VehiclePaginator
from .serializers import MyTokenObtainPairSerializer

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer
from rest_framework.filters import SearchFilter

# Create your views here.


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    # permission_classes = [IsAdminUser, ]


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    pagination_class =VehiclePaginator


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDeleteAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()

class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class =  MilageSerializer

class MotoMilageListAPIView(generics.ListAPIView):
    serializer_class = MotoMilageSerializer
    queryset = Milage.objects.filter(moto__isnull=False)

class MilageListAPIView(generics.ListAPIView):
    serializer_class =  MilageSerializer
    queryset = Milage.objects.all()
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto', )
    ordering_fields = ('year', )

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
