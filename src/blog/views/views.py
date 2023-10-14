from django.shortcuts import render
from rest_framework import generics , viewsets
from blog.models import Post
from blog.serializers.front import DataSerializer
from rest_framework.permissions import IsAdminUser , IsAuthenticatedOrReadOnly

class BlogViewSets(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes=[IsAdminUser]
        else:
            permission_classes=[IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return DataSerializer
            case 'retrieve':
                return DataSerializer
            case _ :
                return DataSerializer