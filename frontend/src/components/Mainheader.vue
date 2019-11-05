<template>
  <div>
    <v-app-bar max-width clipped-left color="warning">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
        <router-link to='/policy/search/' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text">복지정책검색</span>
        </router-link>
        <v-spacer/>

      <router-link to="/notice" style="text-decoration:none;">
        <span class="title ml-3 mr-5 white--text">공지사항</span>
      </router-link>
      <v-spacer />

      <router-link to="/board" style="text-decoration:none;">
        <span class="title ml-3 mr-5 white--text">자유게시판</span>
      </router-link>
      <v-spacer />

      <router-link to="/favorite" style="text-decoration:none;">
        <span class="title ml-3 mr-5 white--text">딱정함</span>
      </router-link>
      <v-spacer />

      <div @click="checkPass" style="text-decoration:none; background: none;">
        <a class="title ml-3 mr-5 white--text">마이페이지</a>
      </div>
    </v-app-bar>
  </div>
</template>

<script>
import router from "../router";
import store from "../store/modules/data.js";
import { mapState, mapActions } from "vuex";

export default {
  data: () => ({
    isLogin: false,
    chkPass: "",
    token: "",
  }),

  async mounted() {
  },
  methods: {
    ...mapActions("data", ["checkPassword"]),
    checkPass() {
      if (this.token !== null) {
        var currentPage = this.$route.fullPath
        if(currentPage != '/mypage'){
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
        }
      } else {
        alert("로그인 후 이용 가능합니다!");
      }
    },
  }
};
</script>