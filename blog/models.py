from pyexpat import model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
