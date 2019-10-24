from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Category, Policy
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
            name = policy.get('name', None)
            Policy(id=id, name=name).save()

        return Response(status=status.HTTP_200_OK)