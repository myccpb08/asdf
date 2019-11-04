<template>
  <div>
    <v-card class="mx-auto">
      <br />
      <img src="../../images/glass_row.png" class="header_left" style="margin-left:2%" />
      <br />
      <v-container fluid grid-list-md pa-2>
        <v-layout>
          <div class="favoritebox">
            <!-- <v-flex class="favoritebox" v-for="i in totalfavorite"> -->
            <div class="favoritecontents">
              찜 해놓은 정책
              <hr />
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="favoritecontent">
                <h4>청년내일채움공제</h4>
              </div>
            </div>
            <div class="favoritecontents">
              진행중인 정책
              <hr />
              <div class="favoritecontent">
                <h4>내집마련 정책</h4>
              </div>
              <div class="favoritecontent">
                <h4>내집마련 정책</h4>
              </div>
              <div class="favoritecontent">
                <h4>내집마련 정책</h4>
              </div>
            </div>
            <div class="favoritecontents">
              결과나온 정책
              <hr />
              <div class="favoritecontent">
                <h4>한 부모 가정 지원</h4>
              </div>
            </div>

            <div class="favoritecontents">
              참여 중 채팅방
              <hr />
              <ul v-for="room in mychat" :key="room.id">
                <li style="text-align:left;">
                  <a @click="goService(room.id)" style="text-decoration:none; color:black">{{room.title}}</a>

                  <v-btn text>
                    <v-icon color="green" @click.stop="room.drawer=!room.drawer">{{icons.chat}}</v-icon>
                  </v-btn>
                  <v-btn text style="padding:0" @click="delChat(room.id)">
                    <v-icon color="red">{{icons.del}}</v-icon>
                  </v-btn>
                </li>
                <br />

                <!-- 채팅 drawer 시작 -->

                <v-navigation-drawer v-model="room.drawer" absolute temporary right width="350">
                  <v-list-item>
                    <v-list-item-avatar>
                      <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>{{room.title}}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-divider></v-divider>
                  <PolicyChat :Id="room.id"></PolicyChat>
                </v-navigation-drawer>
              </ul>
            </div>

            <!-- 채팅 drawer 끝 -->
            <!-- </div>
            </div>-->
          </div>
        </v-layout>
      </v-container>
      <br />
    </v-card>
  </div>
</template>

<script>
import router from "../../router";
import { mdiDelete, mdiChat } from "@mdi/js";
import PolicyChat from "./PolicyChat";

export default {
  data: () => ({
    mychat: [],
    icons: { del: mdiDelete, chat: mdiChat },
    drawer: null
  }),

  components: {
    PolicyChat
  },

  mounted() {
    this.getChatList().then(result => {
      this.mychat = result.data;
    });
  },

  methods: {
    async delChat(chatid) {
      return this.$store
        .dispatch("data/delChatList", chatid)
        .then(result => (this.mychat = result.data));
      window.location.reload();
    },

    async getChatList() {
      return this.$store.dispatch("data/getChatList");
    },

    goService(n) {
      router.push("/detailPolicy/" + n);
    }
  }
};
</script>
<style>
.header_left {
  width: 17%;
}
.favoritebox {
  display: flex;
  text-align: center;
  width: 33.3%;
  min-width: 100%;
  min-height: 400px;
}
.favoritecontents {
  margin: 2%;
  padding: 2%;
  border-radius: 7px;
  min-height: 110px;
  width: 100%;
  border: 4px solid rgb(187, 187, 187);
  text-align: center;
}
.favoritecontent {
  margin: 2%;
  padding: 1%;
  border-radius: 7px;
  width: 40%;
  border: 1px solid gray;
  text-align: center;
  display: inline-flex;
}
</style>