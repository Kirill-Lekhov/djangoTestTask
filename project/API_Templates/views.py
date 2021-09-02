from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ApiTemplateCreateSerializer, ApiTemplateUpdateSerializer
from .permissions import IsOwnerOrReadOnly
from .models import ApiTemplate


class ApiTemplateCreateView(generics.CreateAPIView):
    serializer_class = ApiTemplateCreateSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ApiTemplateUpdateView(generics.UpdateAPIView):
    serializer_class = ApiTemplateUpdateSerializer
    queryset = ApiTemplate.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ApiTemplateDestroyView(generics.DestroyAPIView):
    queryset = ApiTemplate.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ApiTemplateRetrieveView(generics.RetrieveAPIView):
    serializer_class = ApiTemplateCreateSerializer
    queryset = ApiTemplate.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
