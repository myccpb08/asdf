<template>
  <v-app id="app">
    <div class="header">
      <router-link to="/" style="text-decoration:none;">
      <img src="./DdakJeongE.png" style="width:250px;">
<<<<<<< HEAD
      </router-link>
      <v-flex xs6 class="search_form_div">
        <MovieSearchForm :submit="searchMovies" />
      </v-flex>
=======
>>>>>>> 3a52365a2a33c20e383e9caf9dbf20d2d27f496c
    </div>

    <Mainheader/>
    <MainPage/>
     <v-content>
      <!-- <div class="grey lighten-4">
        <v-layout justify-center> -->
          <!-- each pages will be placed here -->
           <router-view />
        <!-- </v-layout>
      </div> -->
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";
import Mainheader from './components/Mainheader'
import MainPage from './components/pages/MainPage'
import MovieSearchForm from './components/MovieSearchForm'

export default {
  components : {
    'MainPage' : MainPage,
    'Mainheader': Mainheader,
    'MovieSearchForm' : MovieSearchForm,
  },

  // data: () => ({
  //   drawer: null,
  //   choices: [
  //     {
  //       icon: "mdi-movie",
  //       text: "영화 검색",
  //       path: "movie-search"
  //     },
  //     {
  //       icon: "mdi-account-supervisor",
  //       text: "회원 리스트",
  //       path: "user-list"
  //     },
  //     {
  //       icon: "mdi-account-arrow-right",
  //       text: "로그인",
  //       path: "login"
  //     },
  //   ]
  // }),



  methods: {
    goTo: function(path) {
      router.push({ name: path });
    }
  }
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}

.header{
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}

.header img{
  position: absolute;
  top: 50%;
  left: 2%;
  transform: translateY(-50%);
}
</style>