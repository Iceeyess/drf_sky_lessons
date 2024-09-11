from django.contrib import admin
from django.urls import path, include

from women import views
from rest_framework import routers

from women.apps import WomenConfig

app_name = WomenConfig.name

# router = routers.SimpleRouter()
# router.register(r'women', views.WomenAPIView, basename='women')

urlpatterns = [
    path('womenlist/', views.WomenAPIList.as_view()),
    path('womenlist/<int:pk>/', views.WomenAPIUpdate.as_view()),
    path('womendetail/<int:pk>/', views.WomenAPIDetailView.as_view()),
]