from django.shortcuts import render
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):

    if request.method == "GET":
        return render(request, 'postmeme/home.html', {'form': PostForm()})

    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Meme has been added to this vast ocean successfully')
        return HttpResponseRedirect(reverse('postmeme-home'))
