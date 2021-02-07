from .serializers import PostSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from postmeme.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
