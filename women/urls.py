from django.contrib import admin
from django.urls import path, include

from women import views
from rest_framework import routers

from women.apps import WomenConfig
from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy

app_name = WomenConfig.name



# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#
#     ]
# router = MyCustomRouter()
# router.register(r'women', views.WomenViewSet, basename='women')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/women/', WomenAPIList.as_view()),
    path('v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    # path('v1/', include(router.urls)),
    # path('womenlist/', views.WomenAPIList.as_view()),
    # path('womenlist/<int:pk>/', views.WomenAPIUpdate.as_view()),
    # path('womenlist/', views.WomenViewSet.as_view({'get': 'list'})),
    # path('womenlist/<int:pk>', views.WomenViewSet.as_view()),
    # path('womenlist/<int:pk>', views.WomenViewSet.as_view({'put': 'update'})),
]