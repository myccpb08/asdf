<template>
  <v-app id="app">
    <template v-if="this.$store.state.data.userPage">
      <div class="header">
        <router-link to="/" style="text-decoration:none;">
          <img src="./images/DdakJeongE.png" style="width:250px;" />
        </router-link>
        <v-spacer></v-spacer>
        <SearchPage></SearchPage>
        <v-spacer></v-spacer>

        <!-- <div style="padding-bottom:100px; padding-right:5px;" v-for="(choice, i) in choices">
          <v-btn
            text
            v-if="(i===1 && isLogin===true) || (i===2 && isLogin===false)"
            :key="i"
            @click="() => {
                if (choice.path) {
                  goTo(choice.path)
                }
              }"
          >
            <v-icon>{{ choice.icon }}</v-icon>
            {{ choice.text }}
          </v-btn>

          <v-btn text :v-if="(i===0 && isLogin===true)" @click="logout">
            <v-icon>{{ choice.icon }}</v-icon>
            {{ choice.text }}
          </v-btn>
        </div> -->
        <div style="padding-bottom:100px; padding-right:5px;">
          <v-btn text v-if="isLogin===false" @click="goTo('Login')">
            <v-icon>{{ choices[2].icon }}</v-icon>
            {{isLogin}}
            {{ choices[2].text }}
          </v-btn>
          <v-btn text v-if="isLogin===true && this.$store.state.user.is_staff===true" @click="logout">
            <v-icon>{{ choices[1].icon }}</v-icon>
            {{isLogin}}
            {{ choices[1].text }}
          </v-btn>
          <v-btn text v-if="isLogin===false" @click="logout">
            <v-icon>{{ choices[0].icon }}</v-icon>
            {{isLogin}}
            {{ choices[0].text }}
          </v-btn>
        </div>
      </div>
      <Mainheader style="position:fixed; z-index:1; width:100%; position: sticky; top: 0;" />
      <v-content>
        <router-view :key="$route.fullPath"/>
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
import Mainheader from "./components/Mainheader";
import MainFooter from "./components/MainFooter";
import SearchPage from "./components/pages/SearchPage";
import { mapActions, mapState } from "vuex";
import store from "./store/modules/data.js";

export default {
  data: () => ({
    isLogin: false,
    chkPass: "",
    token: "",
    choices: [
      {
        icon: "mdi-door",
        text: "로그아웃",
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
      }
    ]
  }),

  components: {
    Mainheader: Mainheader,
    MainFooter: MainFooter,
    SearchPage: SearchPage
  },

  created() {
    console.log("Create!!!!!!!!!!")
    // localStorage.removeItem('token')
    if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null) {
      console.log("Token is not null")
      var result = this.getSession(localStorage.getItem('token')).then(function(value){
        console.log(value)
        console.log(store.state.user)
        console.log(store.state.user.username)
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
    ...mapActions("data", ["logoutUser", "checkPassword"]),
    goTo: function(path) {
      if (store.state.user != null) {
        if (store.state.user.is_staff != true && path == "admin") {
          alert("관계자 외 출입금지 입니다(경고함)");
          router.push("/");
        } else {
          router.push({ name: path });
        }
      } else {
        if (path == "Login") {
          router.push({ name: path });
        } else {
          alert("로그인 후 이용 가능합니다!");
          router.push("/login");
        }
      }
      // router.push({ name: path });
    },
    checkLogin() {
      this.token = localStorage.getItem("token");
      console.log("checkLogin!!");
      if (this.token !== null) {
        this.isLogin = true;
      } else {
        this.isLogin = false;
      }
    },
    checkPass() {
      if (this.token !== null) {
        this.chkPass = prompt("비밀번호를 입력해주세요!", "");
        if (this.chkPass) {
          const params = {
            username: store.state.user.username,
            inputPass: this.chkPass
          };
          this.checkPassword(params).then(result => {
            if (result.data) {
              router.push("/mypage");
            } else {
              alert("비밀번호가 맞지 않습니다!");
            }
          });
        }
      } else {
        alert("로그인 후 이용 가능합니다!");
      }
    },
    async logout() {
      await this.logoutUser();
      window.location.reload("/");
    }
  }
};
</script>

<style>
.v-content__wrap {
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
</style>
