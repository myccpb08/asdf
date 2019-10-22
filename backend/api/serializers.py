from .models import Profile, Movie, User, Post, Notice
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    password = serializers.SerializerMethodField('get_password')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'favorite', 'password')
        
    def get_username(self, obj):
        return obj.user.username

    def get_password(self, obj):
        return obj.user.password

class SessionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_user')
    token = serializers.SerializerMethodField('get_token')
    is_authenticated = serializers.SerializerMethodField(
        'get_is_authenticated')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('username', 'token', 'is_authenticated', 'is_staff')

    def get_user(self, obj):
        return str(obj['username'])

    def get_token(self, obj):
        print(obj['token'])
        return str(obj['token'])

    def get_is_authenticated(self, obj):
        print(obj['is_authenticated'])
        return obj['is_authenticated']

    def get_is_staff(self, obj):
        print(obj['is_authenticated'])
        return obj['is_staff']


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array')

class UserSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'title', 'content')

