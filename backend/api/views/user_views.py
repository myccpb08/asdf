from rest_framework import status
from rest_framework.decorators import api_view
from api.models import create_profile, Profile
from rest_framework.response import Response
from api.serializers import ProfileSerializer



@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        print("enter signup method!!")
        user = request.data.get('user', None)
        username = user.get('username', None)
        password = user.get('password', None)
        favorite = user.get('favoriteValue', None)
        print(user)
        create_profile(username=username, password=password, favortie=favorite)

        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getAllUsers(request):
    print("Enter getAllUser Method")
    profiles = Profile.objects.all()
    print(profiles)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
