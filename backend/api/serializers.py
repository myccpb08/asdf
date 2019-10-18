from .models import Profile, Movie, User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    password = serializers.SerializerMethodField('get_password')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'password', 'email', 'gender', 'location', 'marriage', 'job', 'disability', 'familysize', 'insurance', 'incomequintile')
        
    def get_username(self, obj):
        return obj.user.username

    def get_password(self, obj):
        return obj.user.password


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
