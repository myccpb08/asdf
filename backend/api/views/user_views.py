from rest_framework import status
from rest_framework.decorators import api_view
from api.models import create_profile, create_profile_none, Profile, Policy
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
        lastestView = None
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
                    'lastestView': profile.lastestView,
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
                    'lastestView': profile.lastestView,
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
                'lastestView': None,
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

@api_view(['PUT', 'DELETE', 'POST', 'GET'])
def user(request):
    print("enter user!!")
    if(request.method == 'GET'):
        print("enter user get!!")
        return Response(status=status.HTTP_200_OK)

    if(request.method == 'POST'):
        return Response(status=status.HTTP_200_OK)
    
    if(request.method == 'PUT'):
        print("enter user edit")
        username = request.data.get('username', None)
        name = request.data.get('name', None)
        # password = request.data.get('password', None)
        favorite = request.data.get('favorite', None)
        grade = request.data.get('grade', None)
        
        if grade == "staff":
            is_staff = True
        else: is_staff = False
        
        user = User.objects.get(username=username)
        Profile.objects.filter(user=user).update(
            name=name, favorite=favorite, 
        )
        user.is_staff = is_staff
        user.save()
        
        # user.set_password(password)
        # user.save()

        return Response(status=status.HTTP_200_OK)
    
    if(request.method == 'DELETE'):
        print("Del User!!!!")
        user = request.user
        print(user)
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

@api_view(['PUT', 'GET'])
def latestView(request):
    if request.method == 'GET':
        print("enter latestView Get!!")
        user = request.user
        profile = Profile.objects.get(user=user)
        lv = profile.lastestView.split(' ')
        print(lv)
        lv.pop(0)
        print(lv)
        result = {
            'latestViewList': lv
        }
        print(result)
        return Response(data=result, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        print("enter latestView!!")
        username = request.data.get('username', None)
        path = request.data.get('path', None)
        if path != None:
            path = ' ' + path
       
        user = request.user
        profile = Profile.objects.get(user=user)
        temp = profile.lastestView.split(" ")
        temp.pop(0)
        print(temp)
        print("temp length : ")
        print(len(temp))
        lv = ''
        if len(temp) > 5:
            print("temp is overflow")
            temp.pop(0)
        for t in temp:
            lv += ' ' + t
        print(lv+path)
        Profile.objects.filter(user=user).update(
            lastestView = lv + path
        )
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
                'lastestView': None,
                'token': None,
                'is_authenticated': False,
                'is_staff':  False,
                'pick_policies': None
            }

        else:
            user = User.objects.get(username=username)
            if user.is_authenticated and token == str(Token.objects.get(user=user)):
                result = {
                    'username': username,
                    'name': Profile.objects.get(user=user).name,
                    'favorite': Profile.objects.get(user=user).favorite,
                    'when': Profile.objects.get(user=user).when,
                    'lastestView': Profile.objects.get(user=user).lastestView,
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
                    'lastestView': None,
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
                    'lastestView': Profile.objects.get(user=user).lastestView,
                    'token': token,
                    'is_authenticated': True,
                    'is_staff': Profile.objects.get(user=user).user.is_staff,
                    'pick_policies': Profile.objects.get(user=user).user.pick_policies.all()
                }
        serializer = SessionSerializer(result)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def mychat(request):
    chat_num = request.GET.get('0')
    now_user = request.user
    now_users_chat = now_user.profile.mychat
    now_users_chat += chat_num + ','
    now_user.profile.mychat = now_users_chat
    now_user.profile.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getChatList(request):
    now_user = request.user
    chat_list = now_user.profile.mychat
    chat_list = list(set(chat_list.split(',')))
    print(chat_list)
    data = []
    for i in chat_list:
        if i:
            data += [i]

    data2 = []
    for i in data:
        id = int(i)
        policy = Policy.objects.get(id=id)
        temp = {'id':int(id), 'title':policy.title, 'drawer':False}
        data2 += [temp]
    print(data2)    

    return Response(data=data2, status=status.HTTP_200_OK)

@api_view(['GET'])
def delChat(request):
    chat_num = request.GET.get('0')
    now_user = request.user
    now_users_chat = now_user.profile.mychat
    print(now_users_chat)
    new = ','
    for i in range(1,len(now_users_chat),2):
        if now_users_chat[i] != chat_num:
            print(now_users_chat[i])
            new += (now_users_chat[i]+',')
    now_user.profile.mychat = new
    now_user.profile.save()
    
    chat_list = now_user.profile.mychat
    chat_list = list(set(chat_list.split(',')))
    data = []
    for i in chat_list:
        if i:
            data += [i]

    data2 = []
    for i in data:
        id = int(i)
        policy = Policy.objects.get(id=id)
        temp = {'id':int(id), 'title':policy.title}
        data2 += [temp]   

    return Response(data=data2, status=status.HTTP_200_OK)