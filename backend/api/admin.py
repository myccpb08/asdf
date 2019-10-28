from django.contrib import admin
from .models import Profile, Policy, Category, Category_Policy, Notice, NoticeComment, BoardComment, Board

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite') 

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content')

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class Category_PolicyAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'policy_id')

class NoticeCommentsAdmin(admin.ModelAdmin):
    list_display = ('id','writer', 'post', 'content')

class BoardCommentsAdmin(admin.ModelAdmin):
    list_display = ('id','writer', 'post', 'content')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeComment, NoticeCommentsAdmin)
admin.site.register(BoardComment, BoardCommentsAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Category_Policy, Category_PolicyAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'gender', 'age', 'occupation',) 
