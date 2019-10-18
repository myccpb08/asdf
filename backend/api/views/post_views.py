from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Post, PostComment
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def posts(request):
    return

@api_view(['GET', 'POST', 'DELETE'])
def post_comments(request):
    return