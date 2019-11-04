<template>
  <div>
    <v-card class="mx-auto">
      <br />
        <img src="../../images/glass_row.png" class="header_left" style="margin-left:2%"/>
      <br />
      <v-container fluid grid-list-md pa-2>
        <v-layout>
          <div class="favoritebox">
            <!-- <v-flex class="favoritebox" v-for="i in totalfavorite"> -->
            <div class="favoritecontents">
              찜 해놓은 정책
              <hr />
              <div class="favoritecontent" v-for="pick in pick_policies" :key="pick.id">
                <div class="font-nanum" style="cursor: pointer;" @click="editPickStatus(pick.id)">
                  <h4 >{{ pick.title }}</h4>
                </div>
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
import { mapState, mapActions } from "vuex";
import router from "../../router";
import { mdiDelete, mdiChat } from "@mdi/js";
import PolicyChat from "./PolicyChat";
export default {
  name: "PickPage",
  data: () => ({
    mychat: [],
    icons: { del: mdiDelete, chat: mdiChat },
    drawer: null,
    user: null,
    pick_policies: null
  }),
  components: {
    PolicyChat
  },
  created() {
    this.getPickPolicies();
  },
  mounted() {
    this.getChatList().then(result => {
      this.mychat = result.data;
    });
  },
  methods: {
    // 으아.. Pick, Doing, Finish 각각 다만들어야됨
    getPickPolicies() {
      this.$store.dispatch("data/getPickPolicies").then(result => {
        console.log(result)
        this.pick_policies = result;
      });
    },

    editPickStatus(id){
      // params에 진행중인지 / 결과나온정책인지 추가

      const params ={
        user: this.$store.state.data.user.username,
        policyId: id
      }
      console.log(params)
      this.$store.dispatch("data/editPickPolicies", params)
    },
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
  },
  watch: {
    getRefresh() {
      if (this.user){
        this.getPickPolicies(this.$store.state.data.user.pick_policies);
      }
    }
  },
};
</script>
<style>
.font-nanum {
   font-family: 'Nanum Gothic', sans-serif; 
}
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
  width: 95%;
  border: 1px solid gray;
  text-align: left;
  display: inline-flex;
}

</style>