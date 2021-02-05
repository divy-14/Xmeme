from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    caption = models.TextField(max_length=200)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
