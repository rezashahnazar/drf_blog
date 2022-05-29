from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post


@api_view(['POST'])
def createPost(request):
    if request.method == 'POST':
        result = Post.objects.all()
        return Response(result)
