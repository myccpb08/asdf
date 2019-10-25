from django.contrib import admin
from .models import Profile, Board, Notice, NoticeComment, BoardComment

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite') 

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content')

class NoticeCommentsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'post', 'content')

class BoardCommentsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'post', 'content')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeComment, NoticeCommentsAdmin)
admin.site.register(BoardComment, BoardCommentsAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'gender', 'age', 'occupation',) 
