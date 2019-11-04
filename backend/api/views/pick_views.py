from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Policy, Profile
from rest_framework.response import Response
from api.serializers import PolicySerializer, CategoryPolicySerializer, AllPolicySerializer, PickPolicySerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Blog.objects.filter(pk__in=[1, 4, 7])

@api_view(['GET', 'PUT', 'DELETE'])
def pickPolicies(request):
    # 딱정함에 담긴 정책 id가 넘어옴
    print("딱정함")
    user = request.user;
    if request.method == 'GET':
        policies = []
        pick_policies = user.pick_policies.all()
        serializer = PickPolicySerializer(pick_policies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        # 진행중 정책 / 결과나온 정책 분기문 작성
        params = request.data.get('params')
        policy_id = params.get('policyId')
        now = params.get('now')
        select = params.get('select')
        policy = Policy.objects.get(id=policy_id)
        if select == 1:
            user.doing_policies.add(policy)
            user.pick_policies.remove(policy)

        elif select == 2:
            user.finish_policies.add(policy)
            user.pick_policies.remove(policy)

    elif request.method == 'DELETE':
        policy_id = request.GET.get('policyId')
        policy = Policy.objects.get(id=policy_id)
        user.pick_policies.remove(policy)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def doingPolicies(request):
    user = request.user;
    if request.method == 'GET':
        policies = []
        doing_policies = user.doing_policies.all()
        serializer = PickPolicySerializer(doing_policies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # 진행중 정책 / 결과나온 정책 분기문 작성
        params = request.data.get('params')
        policy_id = params.get('policyId')
        now = params.get('now')
        select = params.get('select')
        policy = Policy.objects.get(id=policy_id)
        if select == 0:
            user.pick_policies.add(policy)
            user.doing_policies.remove(policy)

        elif select == 2:
            user.finish_policies.add(policy)
            user.doing_policies.remove(policy)

    elif request.method == 'DELETE':
        policy_id = request.GET.get('policyId')
        policy = Policy.objects.get(id=policy_id)
        user.doing_policies.remove(policy)

    return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def finishPolicies(request):
    user = request.user;
    if request.method == 'GET':
        policies = []
        finish_policies = user.finish_policies.all()
        serializer = PickPolicySerializer(finish_policies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        # 진행중 정책 / 결과나온 정책 분기문 작성
        params = request.data.get('params')
        policy_id = params.get('policyId')
        now = params.get('now')
        select = params.get('select')
        policy = Policy.objects.get(id=policy_id)
        if select == 0:
            user.pick_policies.add(policy)
            user.finish_policies.remove(policy)

        elif select == 1:
            user.doing_policies.add(policy)
            user.finish_policies.remove(policy)

    elif request.method == 'DELETE':
        policy_id = request.GET.get('policyId')
        policy = Policy.objects.get(id=policy_id)
        user.finish_policies.remove(policy)

    return Response(status=status.HTTP_200_OK)