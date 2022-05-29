from django.urls import path
from .views import postsView, postView, createPostView

urlpatterns = [
    path('post', createPostView),
    path('posts/', postsView),
    path('post/<int:id>', postView)
]
