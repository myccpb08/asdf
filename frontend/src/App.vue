<template>
  <v-app id="app">
    <div class="header">
      <router-link to="/" style="text-decoration:none;">
      <img src="./DdakJeongE.png" style="width:250px;">
      </router-link>
    </div>
    <Mainheader/>
     <v-content>
      <!-- <div class="grey lighten-4">
        <v-layout justify-center> -->
          <!-- each pages will be placed here -->
           <router-view />
        <!-- </v-layout>
      </div> -->
    </v-content>
    <MainFooter />
  </v-app>
</template>

<script>
import router from "./router";
import Mainheader from './components/Mainheader'
import MainFooter from './components/MainFooter'
import MainPage from './components/pages/MainPage'
import { mapActions, mapState, mapGetters } from "vuex";
import store from "./store/modules/data.js";

export default {
  components : {
    'MainPage' : MainPage,
    'Mainheader': Mainheader,
    'MainFooter': MainFooter,
  },
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