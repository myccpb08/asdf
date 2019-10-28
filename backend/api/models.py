from django.db import models
from django.contrib.auth.models import User
import re

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    favorite = models.CharField(max_length=500, default="00")

    # @property
    # def favorite_array(self):
    #     print(re.sub("'[]", '', self.favorite))
    #     return re.sub("'[]", '', self.favorite)


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
        name=kwargs['name'],
        favorite=kwargs['favorite']
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

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class NoticeComment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Notice, on_delete=models.CASCADE)
    content = models.TextField()
    edit = models.BooleanField(default=False)

class BoardComment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    edit = models.BooleanField(default=False)

class Policy(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=500)

class Category(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=500)

class Category_Policy(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    policy_id = models.ForeignKey(Policy, on_delete=models.CASCADE)