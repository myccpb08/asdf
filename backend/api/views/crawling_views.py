from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Category
from rest_framework.response import Response

@api_view(['POST'])
def setCategories(request):
    if request.method == 'POST':
        categories = request.data.get('movies', None)
        for category in categories:
            id = category.get('id', None)
            name = category.get('name', None)

            Category(id=id, name=name).save()

        return Response(status=status.HTTP_200_OK)