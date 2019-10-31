<template>
  <div>
    <v-app-bar max-width clipped-left color="warning">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
        <router-link to='/policy/search/00' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text">복지정책검색</span>
        </router-link>
        <v-spacer/>

        <router-link to='/notice' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text">공지사항</span>
        </router-link>
        <v-spacer/>

        <router-link to='/board' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text">자유게시판</span>
        </router-link>
        <v-spacer/>

        <router-link to='/favorite' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text">딱정함</span>
        </router-link>
        <v-spacer/>

        <!-- <v-btn text large v-on="on">
          로그인
        </v-btn>
        <v-btn text large v-on="on">
          회원가입
        </v-btn> -->
<!--       
        <router-link to='/mypage' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text" >마이페이지</span>
        </router-link> -->
        <div @click="checkPass" style="text-decoration:none; background: none;">
          <a class="title ml-3 mr-5 white--text" >마이페이지</a>
        </div>
   
      <!-- <v-btn text large v-on="on">
        <router-link to='/mypage'>My page</router-link>
      </v-btn> -->
      <!-- <v-btn text large v-on="on">
        <router-link to>딱정함</router-link>
      </v-btn> -->
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app right clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">
        <template v-for="(choice, i) in choices">
            <v-list-item v-if="(i!==2 && isLogin===true) || isLogin===false"
              :key="i"
              @click="() => {
                if (choice.path) {
                  goTo(choice.path)
                }
              }"
            >
              <v-list-item-action>
                <v-icon>{{ choice.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choice.text }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
        </template>
      </v-list>
      
      <template v-if="isLogin" v-slot:append>
        <div class="pa-2">
          <v-btn block dark @click="logout">로그아웃</v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <!-- <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout justify-center align-center> -->
    <!-- each pages will be placed here-->
    <!-- <router-view />
        </v-layout>
      </v-container>
    </v-content>-->
  </div>
</template>

<script>
import router from "../router";
import store from "../store/modules/data.js";
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({
    isLogin: false,
    drawer: null,
    chkPass: "",
    token: "",
    choices: [
      {
        icon: "mdi-movie",
        text: "정책 상세 검색",
        path: "policy-search"
      },
      {
        icon: "mdi-account-supervisor",
        text: "관리자페이지",
        path: "admin"
      },
      {
        icon: "mdi-account-arrow-right",
        text: "로그인",
        path: "Login"
      },
    ]
  }),
  async mounted(){
    this.checkLogin()
  },
  methods: {
    ...mapActions("data", [
      "logoutUser",
      "checkPassword"
    ]),
    goTo: function(path) {
      if(store.state.user!=null){
        if(store.state.user.is_staff!=true && path=='admin'){
          alert('관계자 외 출입금지 입니다(경고함)')
          router.push('/')
        }else{
          router.push({name: path})
        }
      }else{
        if(path=='Login'){
          router.push({name: path})
        }else{
          alert("로그인 후 이용 가능합니다!")
          router.push('/login')
        }
      }
      // router.push({ name: path });
    },
    checkLogin() {
      this.token = localStorage.getItem('token')
      console.log("checkLogin!!")
      if(this.token!==null){
        this.isLogin = true
      }else{
        this.isLogin = false
      }
    },
    checkPass() {
      if(this.token!==null){
        this.chkPass = prompt("비밀번호를 입력해주세요!", "")
        if(this.chkPass){
          const params = {
            username: store.state.user.username,
            inputPass: this.chkPass
          }
          this.checkPassword(params).then((result)=>{
            if(result.data){
              router.push('/mypage')
            }else{
              alert('비밀번호가 맞지 않습니다!')
            }
          })
        }
      }else{
        alert('로그인 후 이용 가능합니다!')
      }
    },
    async logout() {
      await this.logoutUser()
      window.location.reload('/')
    },
  }
};
</script>