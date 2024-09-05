
from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from women.models import Women
from women.serializers import WomenSerializer


# Create your views here.
class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer