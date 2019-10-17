from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, default='M')
    location = models.CharField(max_length=50)
    marriage = models.CharField(max_length=10, default='N')
    job = models.CharField(max_length=50, default='unimployed')
    disability = models.CharField(max_length=10, default='N')
    familysize = models.IntegerField(default=1)
    insurance = models.IntegerField(default=0)
    incomequintile = models.IntegerField(default=1)


#  wrapper for create user Profile
def create_profile(**kwargs):
    print("enter create_profile")
    print(kwargs)
    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )
    print(user)
    profile = Profile.objects.create(
        user=user,
        email=kwargs['email'],
        gender=kwargs['gender'],
        location=kwargs['location'],
        marriage=kwargs['marriage'],
        job=kwargs['job'],
        disability=kwargs['disability'],
        familysize=kwargs['familysize'],
        insurance=kwargs['insurance'],
        incomequintile=kwargs['incomequintile']
    )
    print("finish create_profile")
    return profile

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')


