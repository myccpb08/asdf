from django.contrib import admin
from .models import Profile, Post, Notice

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', ) 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Notice, NoticeAdmin)

# from django.contrib import admin
# from .models import Profile, Post

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'gender', 'age', 'occupation',) 

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content')

# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Post, PostAdmin)
