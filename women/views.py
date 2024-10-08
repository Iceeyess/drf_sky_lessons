
from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from women.models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import AccessToken


# class WomenViewSet(viewsets.ModelViewSet):
#
#     serializer_class = WomenSerializer
#     # renderer_classes = [JSONRenderer]
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

# Create your views here.
# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = [IsAuthenticated, ]

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = [TokenAuthentication, ]


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAdminOrReadOnly, ]
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
    # renderer_classes = [JSONRenderer]

# class WomenAPIView(APIView):
#
#     def get(self, request):
#         w = Women.objects.all().order_by('pk')
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'METHOD PUT NOT ALLOWED'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'OBJECT DOESN\'T EXIST'})
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'METHOD DELETE NOT ALLOWED'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except ObjectDoesNotExist:
#             return Response({'error': 'OBJECT DOESN\'T EXIST'})
#         else:
#             obj = WomenSerializer(instance)
#             Women.objects.get(pk=pk).delete()
#         return Response({'deleted': obj.data})