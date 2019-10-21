from django.contrib import admin
from .models import Profile, Post

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', ) 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)