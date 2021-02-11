from django.shortcuts import render
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from rest_framework.response import Response
from rest_framework import generics, permissions, status


def home(request):

    if request.method == "GET":
        return render(request, 'postmeme/home.html', {'form': PostForm()})

    else:
        form = PostForm(request.POST)
        if form.is_valid():
            user_name = form['name'].value()
            url = form['url'].value()
            caption = form['caption'].value()
            if not Post.objects.filter(name=user_name, caption=caption, url=url).exists():
                form.save()
                messages.success(
                    request, 'Your Meme has been added to this vast ocean successfully')
            else:
                messages.success(
                    request, 'Your doppleganger already posted this meme with the same caption ;(')

        return HttpResponseRedirect(reverse('postmeme-home'))
