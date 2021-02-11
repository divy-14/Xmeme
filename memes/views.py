from .serializers import PostSerializer, PostUpdateSeralizer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, permissions, status
from postmeme.models import Post
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):

        try:
            name = request.data['name']
            url = request.data['url']
            caption = request.data['caption']

            if not Post.objects.filter(name=name, url=url, caption=caption).exists():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)

                # We will replace the original response with this line
                return Response(
                    {'id': serializer.data.get('id')},
                    status=status.HTTP_201_CREATED,
                    headers=headers
                )
            else:
                return Response(status=status.HTTP_409_CONFLICT)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostParticular(generics.RetrieveUpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostUpdateSeralizer
    permission_classes = [permissions.AllowAny]

    # if we are successful in updating we return status code 200
    # else we return status code 404

    # this patch does not allow to change name
    def patch(self, request, pk):
        try:
            testmodel_object = Post.objects.get(pk=pk)
            # set partial=True to update a data partially

            # we do not allow to change names
            if "name" in request.data:
                return Response(status=status.HTTP_403_FORBIDDEN)

            # we change only url and caption
            serializer = PostUpdateSeralizer(
                testmodel_object, data=request.data, partial=True)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
