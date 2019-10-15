from rest_framework import status
from rest_framework.decorators import api_view
from api.models import User
from api.serializers import UserSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE'])
def signup(request):
    print("enter signup!!!")
    if request.method == 'GET':
        print("enter signup if!!!")
        id = request.GET.get('id', request.GET.get('id', None))
        username = request.GET.get('username', None)
        userid = request.GET.get('id', None)
        password = request.GET.get('password', None)

        users = User.objects.all()

        # if id:
        #     movies = movies.filter(pk=id)
        # if title:
        #     movies = movies.filter(title__icontains=title)

        serializer = UserSerializer(users, many=True)
        print("success serializer!!")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        user = User.objects.all()
        user.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        users = request.data.get('users', None)
        for user in users:
            id = user.get('id', None)
            userid = user.get('userid', None)
            username = user.get('username', None)
            password = user.get('password', None)

            if not (id and username):
                continue
            if User.objects.filter(id=id).count() > 0 or User.objects.filter(username=username).count() > 0:
                continue

            User(id=id, userid=userid, username=username, genres=password).save()

        return Response(status=status.HTTP_200_OK)
