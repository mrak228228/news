from django.db import models
from django.conf import settings
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length= 255)
    date = models.DateTimeField (auto_now_add= True)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ("article_detail", kwargs= {"pk": self.pk})
# Create your models here.
