from django.contrib import admin
from django.urls import path, include

from women import views
from rest_framework import routers

from women.apps import WomenConfig

app_name = WomenConfig.name

# router = routers.SimpleRouter()
# router.register(r'women', views.WomenAPIView, basename='women')

urlpatterns = [
    path('womenlist/', views.WomenAPIView.as_view()),
]