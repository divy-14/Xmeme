from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from postmeme.models import Post


def home(request):
    posts = Post.objects.all().order_by('-created')[:100]
    return render(request, 'seememe/home.html', {'posts': posts})


def editMeme(request, meme_pk):
    post = get_object_or_404(Post, pk=meme_pk)
    return render(request, 'seememe/editmeme.html', {'post': post})
