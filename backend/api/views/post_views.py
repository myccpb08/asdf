from rest_framework import status
from rest_framework.decorators import api_view
<<<<<<< HEAD
from api.models import Post, PostComment, Notice
from rest_framework.response import Response
from api.serializers import BoardSerializer

@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'POST':
        print('sksksksksk')
        params = request.data.get('params', None)
        title = params.get('title', None)
        content = params.get('body', None)
        print(title)
        print(content)
        Post.objects.create(title=title, content=content)

        return Response(status=status.HTTP_201_CREATED)
    #post = Post.objects.create(title="제목", content="내용이다")
    #or
    #post = Post(title="제목", content="내용이다")
    #post.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def post_comments(request):
    return

@api_view(['GET'])
def getallnotices(request):
    posts = Notice.objects.all()
    print(posts)
    print('dlddld')
    serializer = BoardSerializer(posts, many=True)
    print(serializer.data)
    return Response(data=serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def getallboards(request):
    posts = Post.objects.all()
    print(posts)
    print('dlddld')
    serializer = BoardSerializer(posts, many=True)
    print(serializer.data)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def notices(request):
    if request.method == 'POST':
        params = request.data.get('params', None)
        title = params.get('title', None)
        content = params.get('body', None)
        Notice.objects.create(title=title, content=content)

        return Response(status=status.HTTP_201_CREATED)
    #post = Post.objects.create(title="제목", content="내용이다")
    #or
    #post = Post(title="제목", content="내용이다")
    #post.save()
    return Response(status=status.HTTP_200_OK)
=======
from api.models import Post, PostComment
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def posts(request):
    return

@api_view(['GET', 'POST', 'DELETE'])
def post_comments(request):
    return
>>>>>>> 3a52365a2a33c20e383e9caf9dbf20d2d27f496c
