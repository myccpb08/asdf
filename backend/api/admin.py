from django.contrib import admin
from .models import Profile, Post, Policy, Category, Category_Policy, Notice


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite') 

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content')

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brief', 'target', 'criteria', 'content', 'supply_way', 'procedure', 'site')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class Category_PolicyAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'policy_id')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Category_Policy, Category_PolicyAdmin)
admin.site.register(Notice, NoticeAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'gender', 'age', 'occupation',) 
