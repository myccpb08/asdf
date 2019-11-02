from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Policy, Category_Policy
from rest_framework.response import Response
from api.serializers import PolicySerializer, CategoryPolicySerializer, AllPolicySerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['GET'])
def getService(request):
    serviceId = int(request.GET.get('0'))
    service = Policy.objects.get(id=serviceId)
    serializer = PolicySerializer(service)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def policySearch(request):
    categoryId = request.GET.get('0')
    print(request.GET.get('0'))

    if(categoryId=="00"):
        service = Policy.objects.all()
        serializer = AllPolicySerializer(service, many=True)
    else:
        service = Category_Policy.objects.filter(category=categoryId)
        serializer = CategoryPolicySerializer(service, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)