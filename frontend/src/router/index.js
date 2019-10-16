import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/MovieSearchPage'
import SignUpPage from '../components/pages/SignUpPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/signup', component: SignUpPage, name: 'SignUp' },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router