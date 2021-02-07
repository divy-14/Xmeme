from rest_framework import serializers
from postmeme.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'caption', 'url']
