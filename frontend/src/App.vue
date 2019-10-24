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
import { mapState, mapActions } from "vuex";

export default {
  components : {
    'MainPage' : MainPage,
    'Mainheader': Mainheader,
    'MainFooter': MainFooter,
  },
  created() {
    console.log("Create!!!!!!!!!!")
    if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
      this.getSession(localStorage.getItem("token"));
    } else {
      //토큰 없을 때
      console.log("token is null")
      router.push("/");
    }
  },
  mounted(){
    this.checkLogin()
  },
  methods: {
    ...mapActions("data", ["getSession"]),
    goTo: function(path) {
      router.push({ name: path });
    },
    checkLogin() {
      console.log("나는 로그인 체크다!!")
      this.token = localStorage.getItem('token')
      if(this.token!==null){
        this.isLogin = true
        console.log("STAFF? : " + store.state.user.is_staff)
      }else{
        this.isLogin = false
      }
    },
  }
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