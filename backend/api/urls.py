from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import post_views
from api.views import user_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('posts/$', post_views.posts, name='post_list'),
    url('posts/comment/$', post_views.post_comments, name='post_comment_list'),
    url('auth/signup/$', user_views.signup, name='sign_up'),
    url('auth/allUsers/$', user_views.getAllUsers, name='get_all_user'),

    # 자유게시판 관련 링크
    url('allboards/$', post_views.getallboards, name="get_all_boards"), # 자유게시판 전체 글 로드
    url('boardDetail/$', post_views.getboard, name="get_board"), # 자유게시판 자세히 & 삭제 & 수정
    url('board/$', post_views.posts, name='boardwrite'), # 자유게시판 작성

    # 공지사항 관련 링크
    url('allnotices/$', post_views.getallnotices, name="get_all_notices"), # 공지사항 전체 글 로드
    url('noticeDetail/$', post_views.getnotice, name="get_notice"), # 공지사항 자세히 & 삭제 & 수정
    url('notice/$', post_views.notices, name='noticewrite'), # 공지사항 작성
]
