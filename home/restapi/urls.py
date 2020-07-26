from django.urls import path, include
from rest_framework import routers
from Blog.api import views
from home.restapi import views

router = routers.DefaultRouter()
router.register(r'jschapters', views.jschaptersViewSet)
router.register(r'jsdescription', views.jsdescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'^api-auth/', include('rest_framework.urls')),
]

# url for our homeapi
# http://127.0.0.1:8000/homeapi/