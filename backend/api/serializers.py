from .models import Profile, Movie, User, Board, Notice, NoticeComment, BoardComment
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    password = serializers.SerializerMethodField('get_password')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'password', 'name', 'favorite')
        
    def get_username(self, obj):
        return obj.user.username

    def get_password(self, obj):
        return obj.user.password

class SessionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_user')
    name = serializers.SerializerMethodField('get_name')
    favorite = serializers.SerializerMethodField('get_favorite')
    token = serializers.SerializerMethodField('get_token')
    is_authenticated = serializers.SerializerMethodField('get_is_authenticated')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    class Meta:
        model = Profile
        fields = ('username', 'name', 'favorite', 'token', 'is_authenticated', 'is_staff')

    def get_user(self, obj):
        return str(obj['username'])

    def get_name(self, obj):
        print(obj['name'])
        return str(obj['name'])

    def get_favorite(self, obj):
        print("obj-favorite")
        print(obj['favorite'])
        return str(obj['favorite'])

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
        model = Board
        fields = ('id', 'title', 'content')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'title', 'content')

class NoticeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeComment
        fields = ('id', 'user', 'post', 'content', 'edit')

class BoardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardComment
        fields = ('id', 'user', 'post', 'content', 'edit')