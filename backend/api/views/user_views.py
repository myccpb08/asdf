from rest_framework import status
from rest_framework.decorators import api_view
from api.models import create_profile
from rest_framework.response import Response



@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        print("enter signup method!!")
        user = request.data.get('user', None)
        username = user.get('username', None)
        email = user.get('email', None)
        password = user.get('password', None)
        print(user)
        create_profile(username=username, password=password, email=email)

        return Response(status=status.HTTP_201_CREATED)
 