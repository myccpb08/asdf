<template>
  <v-app id="app">
    <div class="header">
      <img src="./DdakJeongE.png" style="width:250px;">

      <v-flex xs6 class="search_form_div">
        <MovieSearchForm :submit="searchMovies" />
      </v-flex>
    </div>

    <Mainheader/>

     <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout justify-center align-center>
          <!-- each pages will be placed here -->
           <router-view/>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";
import Mainheader from './components/Mainheader'
import MovieSearchForm from './components/MovieSearchForm'

export default {
  components : {
    'Mainheader': Mainheader,
    'MovieSearchForm' : MovieSearchForm,
  },

  data: () => ({
    drawer: null,
    choices: [
      {
        icon: "mdi-movie",
        text: "영화 검색",
        path: "movie-search"
      }
    ]
  }),



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