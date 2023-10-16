from django.shortcuts import render
from rest_framework import generics , viewsets
from blog.models import Post
from blog.serializers.front import DataSerializer , CreatePostSerializer
from rest_framework.permissions import IsAdminUser , IsAuthenticatedOrReadOnly
from blog.permissions.permissions import IsAuthorOrReadOnly
class BlogViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return DataSerializer
            case 'retrieve':
                return DataSerializer
            case 'create':
                return CreatePostSerializer
            case _ :
                return DataSerializer