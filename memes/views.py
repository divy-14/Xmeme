from .serializers import PostSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions, status
from postmeme.models import Post
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Original Response (inside the `CreateModelMixin` class)
        # return Response(
        #     serializer.data,
        #     status=status.HTTP_201_CREATED,
        #     headers=headers
        # )

        # We will replace the original response with this line
        return Response(
            {'id': serializer.data.get('id')},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class PostParticular(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
