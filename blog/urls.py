from django.urls import path
from .views import postsView, postView, createPostView
from .views2 import PostsList, PostCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('v1/post/', createPostView),
    path('v1/posts/', postsView),
    path('v1/post/<int:id>', postView),

    path('v2/posts/', PostsList.as_view()),
    path('v2/post/create', PostCreate.as_view()),
    path('v2/post/<int:id>', PostRetrieveUpdateDestroy.as_view())
]
