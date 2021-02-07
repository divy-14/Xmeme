from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    caption = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
