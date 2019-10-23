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
        Post.objects.create(title=title, content=content)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)

# 자유게시판 전체 글 불러오기
@api_view(['GET'])
def getallboards(request):
    posts = Post.objects.all()
    serializer = BoardSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# 자유게시판 자세히, 삭제, 수정
@api_view(['GET', 'DELETE', 'POST'])
def getboard(request):
    if request.method == 'POST':
        params = request.data.get('params', None)
        title = params.get('title', None)
        content = params.get('body', None)
        boardid = params.get('id', None)
        item = Post.objects.get(id=boardid)
        item.title = title
        item.content = content
        item.save()
        return Response(status=status.HTTP_201_CREATED)

    else:
        boardid = int(request.GET.get('0'))
        item = Post.objects.get(id=boardid)

        if request.method == 'GET':
            serializer = BoardSerializer(item)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            item.delete()
            return Response(status=status.HTTP_200_OK)

    


''' 여기부터 공지사항 '''
# 공지사항 글쓰기
@api_view(['GET', 'POST', 'DELETE'])
def notices(request):
    if request.method == 'POST':
        params = request.data.get('params', None)
        title = params.get('title', None)
        content = params.get('body', None)
        Notice.objects.create(title=title, content=content)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_200_OK)


# 공지사항 전체 글 불러오기
@api_view(['GET'])
def getallnotices(request):
    posts = Notice.objects.all()
    serializer = NoticeSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# 공지사항 자세히 & 삭제 & 수정
@api_view(['GET', 'DELETE', 'POST'])
def getnotice(request):
    print('안녕')
    if request.method == 'POST':
        params = request.data.get('params', None)
        print(params)
        title = params.get('title', None)
        content = params.get('body', None)
        boardid = params.get('id', None)
        item = Notice.objects.get(id=boardid)
        item.title = title
        item.content = content
        item.save()
        return Response(status=status.HTTP_201_CREATED)
    

    else:
        boardid = int(request.GET.get('0'))
        item = Notice.objects.get(id=boardid)
        if request.method == 'GET':
            serializer = NoticeSerializer(item)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            item.delete()
            return Response(status=status.HTTP_200_OK)

    


''' 여기부터 댓글 '''
# 댓글작성
@api_view(['GET', 'POST', 'DELETE'])
def post_comments(request):
    return