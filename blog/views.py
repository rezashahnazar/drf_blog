from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def hi(request):
    return Response({"message": "hi"})
