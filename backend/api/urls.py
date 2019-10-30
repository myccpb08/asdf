from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import post_views
from api.views import user_views
from api.views import crawling_views
from django.urls import path

urlpatterns = [
    url('auth/signup/$', user_views.signup, name='sign_up'),
    url('auth/allUsers/$', user_views.getAllUsers, name='get_all_user'),
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('auth/checkLogin/$', user_views.login, name='login'),
    url('auth/checkPassword/$', user_views.chkPass, name='chkPass'),
    url('auth/logout/$', user_views.logout, name='logout'),
    url('auth/session/$', user_views.session, name='session'),
    url('auth/user/$', user_views.user, name="user"),

    url('crawling/category/$', crawling_views.setCategories, name='set_categories'),
    
    # 자유게시판 관련 링크
    url('allBoards/$', post_views.getAllBoards, name="get_all_boards"), # 자유게시판 전체 글 로드
    url('boardDetail/$', post_views.getBoard, name="get_board"), # 자유게시판 자세히 & 삭제 & 수정
    url('board/$', post_views.boards, name='boardwrite'), # 자유게시판 작성
    url('getBoardComments/$', post_views.getBoardComments, name='get_borad_comments'), # 자유게시판 댓글 가져오기
    url('boardComment/$', post_views.boardComments, name='board_comment'),

    # 공지사항 관련 링크
    url('allNotices/$', post_views.getAllNotices, name="get_all_notices"), # 공지사항 전체 글 로드
    url('noticeDetail/$', post_views.getNotice, name="get_notice"), # 공지사항 자세히 & 삭제 & 수정
    url('notice/$', post_views.notices, name='noticewrite'), # 공지사항 작성
    url('getNoticeComments/$', post_views.getNoticeComments, name='get_notice_comments'), # 공지사항 댓글 가져오기
    url('noticeComment/$', post_views.noticeComments, name='notice_comment'),
]
