from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Category, Policy, Category_Policy
from rest_framework.response import Response

@api_view(['POST'])
def setCategories(request):
    if request.method == 'POST':
        categories = request.data.get('categories', None)
        for category in categories:
            id = category.get('id', None)
            name = category.get('name', None)
            print("{}, {}".format(id, name))
            Category(id=id, name=name).save()

        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def setPolicies(request):
    if request.method == 'POST':
        policies = request.data.get('policies', None)
        for policy in policies:
            id = policy.get('id', None)
            title = policy.get('title', None)
            brief = policy.get('brief', None)
            target = policy.get('target', None)
            criteria = policy.get('criteria', None)
            content = policy.get('content', None)
            supply_way = policy.get('supply_way', None)
            procedure = policy.get('procedure', None)
            site = policy.get('site', None)
            Policy(id=id, title=title, brief=brief, target=target, criteria=criteria, content=content, supply_way=supply_way, procedure=procedure, site=site).save()

        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def setCategory_Policy(request):
    if request.method == 'POST':
        list = request.data.get('category_policy', None)
        for li in list:
            # category = li.get('category', None)
            # policy = li.get('policy', None)
            category = Category.objects.get(pk=li.get('category', None))
            policy = Policy.objects.get(pk= li.get('policy', None))

            print("{}, {}".format(category.id, policy.id))
            Category_Policy(category=category, policy=policy).save()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_200_OK)