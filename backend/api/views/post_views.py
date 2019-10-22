from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Post, PostComment, Notice
from rest_framework.response import Response
from api.serializers import BoardSerializer, NoticeSerializer

# 자유게시판 글쓰기
@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'POST':
        params = request.data.get('params', None)
        title = params.get('title', None)
        content = params.get('body', None)
        print(title)
        print(content)
        Post.objects.create(title=title, content=content)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)

# 자유게시판 글들 불러오기
@api_view(['GET'])
def getallboards(request):
    posts = Post.objects.all()
    serializer = BoardSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 자유게시판 자세히
@api_view(['GET'])
def getboard(request):
    if request.method == 'GET':
        print(request.GET.get('0'))
        # params = request.GET.get('boardId',None)
        # # params = request.data.get('params', None)
        # print(params)
        print(1234)
        boardid = int(request.GET.get('0'))
        # print(boardid)
        item = Post.objects.get(id=boardid)
        serializer = BoardSerializer(item)
        print('여긴어디나는누구')
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# 공지사항 글쓰기
@api_view(['GET', 'POST'])
def notices(request):
    if request.method == 'POST':
        params = request.data.get('params', None)
        title = params.get('title', None)
        content = params.get('body', None)
        Notice.objects.create(title=title, content=content)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)

# 공지사항 글들 불러오기
@api_view(['GET'])
def getallnotices(request):
    posts = Notice.objects.all()
    print(posts)
    print('dlddld')
    serializer = NoticeSerializer(posts, many=True)
    print(serializer.data)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 공지사항 자세히
@api_view(['GET'])
def getnotice(request):
    if request.method == 'GET':
        noticeid = request.GET.get("noticeid", None)
        item = Notice.objects.get(noticeid=noticeid)
        serializer = NoticeSerializer(item)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


# 댓글작성
@api_view(['GET', 'POST', 'DELETE'])
def post_comments(request):
    return