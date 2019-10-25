<template>
  <v-app id="app">
    <template v-if="this.$store.state.data.userPage">
      <div class="header">
        <router-link to="/" style="text-decoration:none;">
          <img src="./DdakJeongE.png" style="width:250px;" />
        </router-link>
      </div>
      <Mainheader />
      <v-content>
        <router-view />
      </v-content>
    </template>

    <template v-else>
      <router-view />
    </template>
    <MainFooter />
  </v-app>
</template>

<script>
import router from "./router";
import Mainheader from './components/Mainheader'
import MainFooter from './components/MainFooter'
<<<<<<< HEAD
import MainPage from './components/pages/MainPage'
import { mapActions, mapState, mapGetters } from "vuex";
import store from "./store/modules/data.js";
=======
>>>>>>> fd88dd8d31338ca1e494491ebe59d57a1fffa0ec

export default {
  components : {
    'Mainheader': Mainheader,
    'MainFooter': MainFooter,
  },
<<<<<<< HEAD
=======
  data: () => ({}),
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
>>>>>>> fd88dd8d31338ca1e494491ebe59d57a1fffa0ec
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}

.header {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}

.header img {
  position: absolute;
  top: 50%;
  left: 2%;
  transform: translateY(-50%);
}
</style>