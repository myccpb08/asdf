from django.contrib import admin
from .models import Profile, Post, Notice

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite') 

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Notice, NoticeAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'gender', 'age', 'occupation',) 