from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Policy, Profile
from rest_framework.response import Response
from api.serializers import PolicySerializer, CategoryPolicySerializer, AllPolicySerializer
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Blog.objects.filter(pk__in=[1, 4, 7])

@api_view(['GET', 'PUT', 'DELETE'])
def pickPolicies(request):
    # 딱정함에 담긴 정책 id가 넘어옴
    print("딱정함")
    if request.method == 'GET':
        policies = []
        user = request.user;
        pick_policies = user.pick_policies.all()
        serializer = PolicySerializer(pick_policies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        # 진행중 정책 / 결과나온 정책 분기문 작성
        params = request.data.get('params')
        policy_id = params.get('policyId')
        user = User.objects.get(username=request.user)
        policy = Policy.objects.get(id=policy_id)
        print(policy)
        user.doing_policies.add(policy)
        for i in user.doing_policies.all():
            print(i)
        print()
        for i in user.pick_policies.all():
            print(i)
        print()
        # 인자 넣어야 삭제됨
        user.pick_policies.remove()
        for i in user.pick_policies.all():
            print(i)
        print()
    else:
        pass
    return Response(status=status.HTTP_200_OK)