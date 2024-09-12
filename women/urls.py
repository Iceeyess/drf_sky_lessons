from django.contrib import admin
from django.urls import path, include

from women import views
from rest_framework import routers

from women.apps import WomenConfig

app_name = WomenConfig.name

router = routers.SimpleRouter()
router.register(r'women', views.WomenViewSet, basename='women')

urlpatterns = [
    path('v1/', include(router.urls)),

    # path('womenlist/', views.WomenAPIList.as_view()),
    # path('womenlist/<int:pk>/', views.WomenAPIUpdate.as_view()),
    # path('womenlist/', views.WomenViewSet.as_view({'get': 'list'})),
    # path('womenlist/<int:pk>', views.WomenViewSet.as_view()),
    # path('womenlist/<int:pk>', views.WomenViewSet.as_view({'put': 'update'})),
]