from rest_framework import status
from rest_framework.decorators import api_view
from api.models import create_profile, Profile
from rest_framework.response import Response
from api.serializers import ProfileSerializer

def putCategory():
    test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId=01&pageUnit=10&pageIndex=1"
    resp = requests.get(test_url)
    html = BeautifulSoup(resp.content, 'html.parser')
    lis = html.find('div', {'class': 'catBoxIn'}).findAll('a')
    for li in lis:
        categoryNum = li.get('href')[29:-7]
        name = li.get('title')
        category = Category.objects.create(id= categoryNum, name=name)
        category.save()



@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        print("enter signup method!!")
        user = request.data.get('user', None)
        username = user.get('username', None)
        email = user.get('email', None)
        password = user.get('password', None)
        gender = user.get('gender', None)
        location = user.get('location', None)
        marriage = user.get('marriage', None)
        job = user.get('job', None)
        disability = user.get('disability', None)
        familysize = user.get('familysize', None)
        insurance = user.get('insurance', None)
        incomequintile = user.get('incomequintile', None)
        print(user)
        create_profile(username=username, password=password, email=email, gender=gender, location=location, marriage=marriage, job=job, disability=disability,
        familysize=familysize, insurance=insurance, incomequintile=incomequintile)

        return Response(status=status.HTTP_201_CREATED)



@api_view(['GET'])
def getAllUsers(request):
    profiles = Profile.objects.all()
    print(profiles)
    serializer = ProfileSerializer(profiles, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
