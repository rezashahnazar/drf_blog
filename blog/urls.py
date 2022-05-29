from django.urls import path
from .views import createPost

urlpatterns = [
    path('post', createPost),
    # path('posts/', ),
    # path('post/<int:id>',)
]
