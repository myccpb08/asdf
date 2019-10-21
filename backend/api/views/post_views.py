from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Post, PostComment
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'POST':
        title = request.data.get('title', None)
        contetn = request.data.get('body', None)
        Post.objects.create(title="제목", content="내용이다")

        return Response(status=status.HTTP_201_CREATED)
    #post = Post.objects.create(title="제목", content="내용이다")
    #or
    #post = Post(title="제목", content="내용이다")
    #post.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def post_comments(request):
    return