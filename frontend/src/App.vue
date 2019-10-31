<template>
  <v-app id="app">
    <template v-if="this.$store.state.data.userPage">
      <div class="header">
        <router-link to="/" style="text-decoration:none;">
          <img src="./images/DdakJeongE.png" style="width:250px;" />
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
import { mapActions } from "vuex";
import store from "./store/modules/data.js";

export default {
  components : {
    'Mainheader': Mainheader,
    'MainFooter': MainFooter,
  },
  // created() {
  //   console.log("Create!!!!!!!!!!")
  //   if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
  //     var result = this.getSession(localStorage.getItem('token')).then(function(value){
  //       console.log(value)
  //       if(value==false){
  //         router.push('/')
  //       }
  //     });
  //   }
  //   else{
  //     router.push("/");
  //   }
  // },
  methods: {
    ...mapActions("data", ["getSession"]),
  }

};
</script>

<style>
.v-content__wrap{
  display: flex;
  justify-content: center;
  align-items: center;
}

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