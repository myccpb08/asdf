<template>
  <v-app id="app">
    <template v-if="this.$store.state.data.userPage">
      <div class="header">
        <router-link to="/" style="text-decoration:none;">
          <img src="./images/DdakJeongE.png" style="width:250px;" />
        </router-link>
        <SearchPage></SearchPage>
      </div>
      <Mainheader style="position:fixed; z-index:1; width:100%; position: sticky; top: 0;" />
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
import SearchPage from "./components/pages/SearchPage";
import { mapActions } from "vuex";
import store from "./store/modules/data.js";
// import Firebaseservice from './services/FirebaseService'

export default {
  
  components : {
    'Mainheader': Mainheader,
    'MainFooter': MainFooter,
    'SearchPage': SearchPage,
  },
  created() {
    console.log("Create!!!!!!!!!!")
    if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
      var result = this.getSession(localStorage.getItem('token')).then(function(value){
        console.log(value)
        if(value==false){
          router.push('/')
        }
      });
    }
    else{
      router.push("/");
    }
  },
  created() {
    console.log("Create!!!!!!!!!!")
    if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
      var result = this.getSession(localStorage.getItem('token')).then(function(value){
        console.log(value)
        if(value==false){
          router.push('/')
        }
      });
    }
    else{
      router.push("/");
    }
  },
  methods: {
    ...mapActions("data", ["getSession"]),
  }

};
</script>

<style>
.v-content__wrap{
  display: table;
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
.v-toolbar__content{
      height: 45px !important;
}

</style>