<template>
  <div>
    <v-app-bar max-width clipped-left color="warning">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
        <router-link to='/policy/search' style="text-decoration:none;">
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
      
        <router-link to='/mypage' style="text-decoration:none;">
          <span class="title ml-3 mr-5 white--text" >마이페이지</span>
        </router-link>
   
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
          <v-list-item
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
      
      <template v-slot:append>
        <div class="pa-2">
          <v-btn block dark>로그아웃</v-btn>
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

export default {
  data: () => ({
    drawer: null,
    choices: [
      {
        icon: "mdi-movie",
        text: "정책 상세 검색",
        path: "policy-search"
      },
      {
        icon: "mdi-account-supervisor",
        text: "회원 리스트",
        path: "user-list"
      },
      {
        icon: "mdi-account-arrow-right",
        text: "로그인",
        path: "Login"
      },
    ]
  }),

  methods: {
    goTo: function(path) {
      router.push({ name: path });
    }
  }
};
</script>