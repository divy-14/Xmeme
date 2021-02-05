from django.shortcuts import render
from django.http import HttpResponse
from postmeme.models import Post


def home(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'seememe/home.html', {'posts': posts})
