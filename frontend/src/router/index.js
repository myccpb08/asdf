import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import Mypage from '../components/pages/Mypage'
import AdminPage from '../components/pages/AdminPage'
import SignUpPage from '../components/pages/SignUpPage'
import LoginPage from '../components/pages/LoginPage'
import NoticePage from '../components/pages/NoticePage'
import PolicySearchPage from '../components/pages/PolicySearchPage'
import NoticeDetailPage from '../components/pages/NoticeDetailPage'
import NoticeWritePage from '../components/pages/NoticeWritePage'
import NoticeUpdatePage from '../components/pages/NoticeUpdatePage'
import BoardPage from '../components/pages/BoardPage'
import BoardWritePage from '../components/pages/BoardWritePage'
import BoardDetailPage from '../components/pages/BoardDetailPage'
import BoardUpdatePage from '../components/pages/BoardUpdatePage'
import FavoritePage from '../components/pages/FavoritePage'

import Chat from '../components/pages/Chat'

import DetailPolicyPage from '../components/pages/DetailPolicyPage'
// admin
import DashBoard from "../admins/DashBoard.vue"
import UserList from "../admins/UserList.vue"
import PolicyList from "../admins/PolicyList.vue"
import NoticeList from "../admins/NoticeList.vue"
import BoardList from "../admins/BoardList.vue"

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/mypage', component: Mypage, name:'mypage'},
    { path: '/signup', component: SignUpPage, name: 'SignUp' },
    { path: '/login', component: LoginPage, name: 'Login'},
    { path: '/notice', component: NoticePage, name: 'Notice'},
    { path: '/policy/search/:categoryId', component: PolicySearchPage, name: 'PolicySearch'},
    { path: '/notice/write', component: NoticeWritePage, name: 'NoticeWrite'},
    { path: '/board', component: BoardPage, name: 'Board'},
    { path: '/board/write', component: BoardWritePage, name: 'BoardWrite'},
    { path: '/favorite', component: FavoritePage, name: 'Favorite'},

    { path: '/detailPolicy/:policyId', component: DetailPolicyPage, name: 'DetailPolicy', props: true},
    { path: '/boardDetail/:boardId',component: BoardDetailPage, name: 'boardDetail', props: true},
    { path: '/boardupdate/:boardId', component: BoardUpdatePage, name:'boardUpdate', props:true},
    { path: '/noticeupdate/:noticeId', component: NoticeUpdatePage, name:'noticeUpdate', props:true},
    { path: '/noticeDetail/:noticeId',component: NoticeDetailPage, name: 'noticeDetail', props: true},
    { path: '/chat',component: Chat, name: 'chat', props: true},
    { 
      path: '/admin', 
      component: AdminPage, 
      name: "admin",
      children:[
        {
          path: '/',
          name : "dashboard",
          component : DashBoard
        },
        {
          path: 'user',
          name : 'user-list',
          component : UserList
        },
        {
          path: 'policy',
          name : 'policy',
          component : PolicyList
        },
        {
          path: "notice",
          name : "/notice-list",
          component : NoticeList
        },
        {
          path: "board",
          name : "/board-list",
          component : BoardList
        },
      ]
    },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router 