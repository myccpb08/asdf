<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>

      <!-- 검색 폼 -->
      <v-flex xs6>
        <SearchForm :submit="searchPolicy" v-on:reload="reload()"/>
      </v-flex>

      <!-- 검색 결과 -->
      <!-- <v-flex xs7>
        <MovieList :movie-list-cards="movieList" />
      </v-flex> -->

    </v-layout>
  </v-container>

</template>

<script>
import { mapState, mapActions } from "vuex";
import SearchForm from "./SearchForm";
// import MovieList from "../MovieList";

export default {
  components: { 
      SearchForm 
    },
  data: () => ({}),
//   computed: { 
//       ...mapState({ 
//           movieList: state => state.data.movieSearchList 
//         }) 
//     },
  methods: {
    ...mapActions("data", ["searchPolicy"]),
    async reload(){
      console.log('들어옴?')
    },
}};
</script>