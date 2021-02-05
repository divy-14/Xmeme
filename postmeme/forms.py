from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['caption'].widget.attrs['placeholder'] = 'Enter a small catching caption'
        self.fields['url'].widget.attrs['placeholder'] = 'Enter meme url'

    class Meta:
        model = Post
        fields = [
            'name',
            'caption',
            'url',
        ]
