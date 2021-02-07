from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from postmeme.models import Post
from django.contrib import messages
from postmeme.forms import PostForm, PostPartialForm
from django.urls import reverse


def home(request):
    posts = Post.objects.all().order_by('-created')[:100]
    return render(request, 'seememe/home.html', {'posts': posts})


def editMeme(request, meme_pk):
    post = Post.objects.get(id=meme_pk)

    if request.method == "GET":
        return render(request, 'seememe/editmeme.html', {'form': post})

    else:
        form = PostPartialForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Meme edited successfully :)')
        return HttpResponseRedirect("#")
