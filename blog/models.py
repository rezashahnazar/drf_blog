from pyexpat import model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=16)
    content = models.TextField()
