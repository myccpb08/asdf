from rest_framework import status
from rest_framework.decorators import api_view
from api.models import create_profile, create_profile_none, Profile
from rest_framework.response import Response
from api.serializers import ProfileSerializer, SessionSerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        print("enter signup method!!")
        user = request.data.get('user', None)
        username = user.get('username', None)
        password = user.get('password', None)
        name = user.get('name', None)
        favorite = user.get('favoriteValue', None)
        when = None
        print(user)
        if favorite=="":
            favorite=None
            create_profile_none(username=username, password=password, name=name)
        else:
            create_profile(username=username, password=password, name=name, favorite=favorite)

        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getAllUsers(request):
    print("Enter getAllUser Method")
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        print("enter login function!!")
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        print("username : " + username + "  password : " + password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            print("user is true")
            auth.login(request, user)
            token = Token.objects.filter(user=user)

            if token:   # 토큰 True
                print("token is true")
                if str(token[0]) in request.session:
                    del request.session[str(token[0])]
                user.auth_token.delete()
                
                newToken = Token.objects.create(user=user)
                request.session[str(newToken)] = username
                profile = Profile.objects.get(user=user)
                print("favorite : " + profile.favorite)
                print(profile.when)
                result = {
                    'username': username,
                    'name': profile.name,
                    'favorite': profile.favorite,
                    'when': profile.when,
                    'token': newToken,
                    'is_staff': profile.user.is_staff,
                    'is_authenticated': True
                }
            else:
                token = Token.objects.create(user=user)  # 토큰 생성
                request.session[str(token)] = username  # 토큰에 해당하는 user명을 세션에 저장
                profile = Profile.objects.get(user=user)
                print("favorite : " + profile.favorite)
                result = {
                    'username': username,
                    'name': profile.name,
                    'favorite': profile.favorite,
                    'when': profile.when,
                    'token': token,
                    'is_staff': profile.user.is_staff,
                    'is_authenticated': True
                }
        else:
            print("user is false")
            result = {
                'username': None,
                'name': None,
                'favorite': None,
                'when': None,
                'token': None,
                'is_staff': False,
                'is_authenticated': False
            }

        serializer = SessionSerializer(result)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def chkPass(request):
    if request.method == 'POST':
        print("enter user_views chkPass!")
        username = request.data.get('username', None)
        password = request.data.get('inputPass', None)
        print("username : " + username + "  password : " + password)
        user = auth.authenticate(username=username, password=password)
        if user:
            result=True
        else:
            result=False
        return Response(data=result, status=status.HTTP_200_OK)

@api_view(['PUT', 'DELETE'])
def user(request):
    print("enter user!!")
    if(request.method == 'GET'):
        print("enter user get!!")
        return Response(status=status.HTTP_200_OK)
    
    if(request.method == 'PUT'):
        print("enter user edit")
        username = request.data.get('username', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)
        favorite = request.data.get('favorite', None)
        grade = request.data.get('grade', None)
        
        if grade == "staff":
            is_staff = True
        else: is_staff = False
        
        print(username + " " + name + " " + password + " ")
        user = User.objects.get(username=username)
        print(user.is_staff)
        print("PPPPP : " + password)
        Profile.objects.filter(user=user).update(
            name=name, favorite=favorite, 
        )
        user.is_staff = is_staff
        user.save()
        
        # user.set_password(password)
        # user.save()

        return Response(status=status.HTTP_200_OK)
    
    if(request.method == 'DELETE'):
        print(1111)
        username = request.GET.get('username', None)
        user = User.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request):
    if request.method == "POST":
        username = request.data.get('username', None)
        user = User.objects.get(username=username)
        token = Token.objects.get(user=user)
        del request.session[str(token)]
        user.auth_token.delete()
        auth.logout(request)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST', 'PUT'])
def session(request):
    if request.method == "POST":
        print("enter in session function")
        token = request.data.get('token', None)
        username = request.session.get(str(token), None)
        if username == None:
            result = {
                'username': None,
                'name': None,
                'favorite': None,
                'when': None,
                'token': None,
                'is_authenticated': False,
                'is_staff':  False,
                'pick_policies': False
            }

        else:
            user = User.objects.get(username=username)
            if user.is_authenticated and token == str(Token.objects.get(user=user)):
                result = {
                    'username': username,
                    'name': Profile.objects.get(user=user).name,
                    'favorite': Profile.objects.get(user=user).favorite,
                    'when': Profile.objects.get(user=user).when,
                    'token': token,
                    'is_authenticated': True,
                    'is_staff': Profile.objects.get(user=user).user.is_staff,
                    'pick_policies': Profile.objects.get(user=user).user.pick_policies.all()
                }
            else:
                result = {
                    'username': None,
                    'name': None,
                    'favorite': None,
                    'when': None,
                    'token': None,
                    'is_authenticated': False,
                    'is_staff':  False,
                    'pick_policies': False
                }
        serializer = SessionSerializer(result)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        print('session put')
        token = request.data.get('token', None)
        username = request.session.get(str(token), None)
        user = User.objects.get(username=username)
        if user.is_authenticated and token == str(Token.objects.get(user=user)):
                result = {
                    'username': username,
                    'name': Profile.objects.get(user=user).name,
                    'favorite': Profile.objects.get(user=user).favorite,
                    'when': Profile.objects.get(user=user).when,
                    'token': token,
                    'is_authenticated': True,
                    'is_staff': Profile.objects.get(user=user).user.is_staff,
                    'pick_policies': Profile.objects.get(user=user).user.pick_policies.all()
                }
        serializer = SessionSerializer(result)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


