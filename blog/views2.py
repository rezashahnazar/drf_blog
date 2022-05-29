from .models import Post
from .seliralizers import PostSerializer
from rest_framework import generics


class PostsList(generics.ListAPIView):
    queryset = Post.objects.order_by('id').reverse()
    serializer_class = PostSerializer
    filterset_fields = ['id', 'title', 'content']


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
