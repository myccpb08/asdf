from django.db import models
from django.contrib.auth.models import User
from datetime import date
import re


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    favorite = models.CharField(max_length=500, default="00")
    when = models.DateTimeField(default=date.today())

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
    # print(kwargs['favorite'])
    profile = Profile.objects.create(
        user=user,
        name=kwargs['name'],
        favorite=kwargs['favorite']
    )
    print("finish create_profile")
    return profile

def create_profile_none(**kwargs):
    print("enter create_profile_none")
    print(kwargs)
    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )
    print(user)
    # print(kwargs['favorite'])
    profile = Profile.objects.create(
        user=user,
        name=kwargs['name']
    )
    print("finish create_profile")
    return profile


class Notice(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    clicked = models.IntegerField(default=0)
    when = models.DateTimeField(default=date.today())

class Board(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    clicked = models.IntegerField(default=0)
    when = models.DateTimeField(default=date.today())

class NoticeComment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Notice, on_delete=models.CASCADE)
    content = models.TextField()
    edit = models.BooleanField(default=False)
    when = models.DateTimeField(default=date.today())

class BoardComment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    edit = models.BooleanField(default=False)
    when = models.DateTimeField(default=date.today())

class Policy(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    title = models.TextField()
    brief = models.TextField()
    target = models.TextField()
    criteria = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    supply_way = models.TextField(null=True, blank=True)
    procedure = models.TextField(null=True, blank=True)
    site =models.TextField(null=True, blank=True)


class Category(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=500)

class Category_Policy(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)