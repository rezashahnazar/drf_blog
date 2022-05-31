from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Post
from .seliralizers import PostSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def ListPostView(request):
    if request.method == 'GET':
        result = Post.objects.all()
        serialized_result = PostSerializer(result, many=True)
        return Response(serialized_result.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def RetrieveUpdateDestroyPostView(request, id):
    try:
        result = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized_result = PostSerializer(result)
        return Response(serialized_result.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        data = request.data
        serialized_data = PostSerializer(result, data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def CreatePostView(request):
    if request.method == 'POST':
        user = request.user.id
        data = request.data
        data['author'] = user
        serialized_data = PostSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
