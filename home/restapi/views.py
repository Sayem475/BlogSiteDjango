from django.shortcuts import render 
from home.models import jschapters, jsdescription
from rest_framework import permissions
from rest_framework import viewsets
from home.restapi.serializers import jschaptersSerializer, jsdescriptionSerializer


class jschaptersViewSet(viewsets.ModelViewSet):
    queryset = jschapters.objects.all()
    serializer_class = jschaptersSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class jsdescriptionViewSet(viewsets.ModelViewSet):
    queryset = jsdescription.objects.all()
    serializer_class = jsdescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]