from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Policy, Category_Policy
from rest_framework.response import Response
from api.serializers import PolicySerializer, CategoryPolicySerializer, AllPolicySerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['GET', 'PUT'])
def getService(request):
    if request.method == 'GET':
        serviceId = int(request.GET.get('0'))
        service = Policy.objects.get(id=serviceId)
        serializer = PolicySerializer(service)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        params = request.data.get('params')
        policy_id = params.get('id')
        # print(request.user)
        # print(User.objects.all())
        user = User.objects.get(username=request.user)
        policy = Policy.objects.get(id=policy_id)
        print(user.pick_policies.all())
        if policy in user.pick_policies.all():
            user.pick_policies.remove(policy)
        else:
            user.pick_policies.add(policy)
        print(user.pick_policies.all())
        return Response(status=status.HTTP_200_OK)


@api_view(['GET',])
def policySearch(request):
    categoryId = request.GET.get('0')
    print(111111)
    print(request.GET.get('0'))

    if(categoryId=="00"):
        service = Policy.objects.all()
        serializer = AllPolicySerializer(service, many=True)
    else:
        service = Category_Policy.objects.filter(category=categoryId)
        serializer = CategoryPolicySerializer(service, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def policyClicked(request):
    policyid = int(request.GET.get('0'))
    item = Policy.objects.get(id=policyid)
    item.clicked += 1
    item.save()
    return Response(status=status.HTTP_200_OK)