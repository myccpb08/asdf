from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import post_views
from api.views import user_views
from api.views import crawling_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('posts/$', post_views.posts, name='post_list'),
    url('posts/comment/$', post_views.post_comments, name='post_comment_list'),
    
    url('auth/signup/$', user_views.signup, name='sign_up'),
    url('auth/allUsers/$', user_views.getAllUsers, name='get_all_user'),

    url('crawling/category/$', crawling_views.setCategories, name='set_categories'),
    url('board/$', post_views.posts, name='boardwrite'),
    url('allboards/$', post_views.getallboards, name="get_all_boards"),
    url('boardDetail/$', post_views.getboard, name="get_board"),
    url('allnotices/$', post_views.getallnotices, name="get_all_notices"),
    url('notice/$', post_views.notices, name='noticewrite'),
]
