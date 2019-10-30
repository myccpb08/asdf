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
        inputFavorite = str(obj['favorite'])
        strFavorite = inputFavorite.replace('\', \'', " ").strip('[\'\']')
        objFavorite = strFavorite.split(" ")
        convertFavorite = {}
        for f in objFavorite:
            if f=='00':
                convertFavorite['00']='등록된 관심 카테고리가 없습니다..'
                break
            elif f=='01':
                convertFavorite['01']='임신/출산'
            elif f=='02':
                convertFavorite['02']='영유아'
            elif f=='03':
                convertFavorite['03']='아동/청소년'
            elif f=='04':
                convertFavorite['04']='청년'
            elif f=='05':
                convertFavorite['05']='중장년'
            elif f=='06':
                convertFavorite['06']='노년'
            elif f=='07':
                convertFavorite['07']='장애인'
            elif f=='08':
                convertFavorite['08']='한부모'
            elif f=='09':
                convertFavorite['09']='다문화(새터민)'
            elif f=='10':
                convertFavorite['10']='저소득층'
            elif f=='11':
                convertFavorite['11']='교육'
            elif f=='12':
                cconvertFavorite['12']='고용'
            elif f=='13':
                convertFavorite['13']='주거'
            elif f=='14':
                convertFavorite['14']='건강'
            elif f=='15':
                convertFavorite['15']='서민금융'
            elif f=='16':
                convertFavorite['16']='문화'
        return convertFavorite

    def get_token(self, obj):
        print(obj['token'])
        return str(obj['token'])

    def get_is_authenticated(self, obj):
        print(obj['is_authenticated'])
        return obj['is_authenticated']

    def get_is_staff(self, obj):
        print(obj['is_staff'])
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