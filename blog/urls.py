from django.urls import path
from .views1 import ListPostView, RetrieveUpdateDestroyPostView, CreatePostView
from .views2 import PostsList, PostCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('v1/posts/create', CreatePostView),
    path('v1/posts/list', ListPostView),
    path('v1/posts/post/<int:id>', RetrieveUpdateDestroyPostView),

    path('v2/posts/create', PostCreate.as_view()),
    path('v2/posts/list', PostsList.as_view()),
    path('v2/posts/post/<int:id>', PostRetrieveUpdateDestroy.as_view())
]
