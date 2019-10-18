import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import AdminPage from '../components/pages/AdminPage'
import SignUpPage from '../components/pages/SignUpPage'
import LoginPage from '../components/pages/LoginPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/user/list', component: AdminPage, name: "user-list"},
    { path: '/signup', component: SignUpPage, name: 'SignUp' },
    { path: '/login', component: LoginPage, name: 'Login'}
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router