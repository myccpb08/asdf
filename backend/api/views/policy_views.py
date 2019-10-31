from rest_framework import status
from rest_framework.decorators import api_view
from api.models import create_profile, Profile
from rest_framework.response import Response
from api.serializers import ProfileSerializer, SessionSerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['GET'])
def getAllUsers(request):
    print("Enter getAllUser Method")
    profiles = Profile.objects.all()
    print(profiles)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)