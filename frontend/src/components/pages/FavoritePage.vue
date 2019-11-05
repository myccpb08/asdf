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
              <div class="favoritecontent" v-for="pick in pick_policies" :key="pick.id">
                <div class="font-nanum" style="cursor: pointer;" @click="pick.modal = true">
                  <h4>{{ pick.title }}</h4>
                </div>
                <FavoriteModal v-if="pick.modal" @close="pick.modal = false">
                                <!-- you can use custom content here to overwritedefault content-->
                  <h3 slot="header">
                    {{ pick.title }}
                    <v-divider />
                  </h3>

                  <div slot="body">
                    <div class="row">
                      <div class="col">
                      <v-btn outlined color="#42b983" @click="goService(pick.id)">상세보기</v-btn>
                      </div>
                      <div >
                        <v-radio-group v-model="radio_pick">
                          <v-radio v-for="(n, i) in selects" :key="i" :label="n" :value="i"></v-radio>
                        </v-radio-group>
                      </div>
                    </div>
                  </div>
                  <div slot="footer">
                    <button @click="pickSave(pick, 0, radio_pick)" style="width:33%" >저장</button>
                    <button @click="pickDelete(pick, 0)" style="width:33%">삭제</button>
                    <button @click="pick.modal = false; radio_pick=0" style="width:33%">닫기</button>
                  </div>
                </FavoriteModal>
              </div>
            </div>
            <div class="favoritecontents">
              진행중인 정책
              <hr />
              <div class="favoritecontent" v-for="pick in doing_policies" :key="pick.id">
                <div class="font-nanum" style="cursor: pointer;" @click="pick.modal = true">
                  <h4>{{ pick.title }}</h4>
                </div>
                <FavoriteModal v-if="pick.modal" @close="pick.modal = false">
                                <!-- you can use custom content here to overwritedefault content-->
                  <h3 slot="header">
                    {{ pick.title }}
                    <v-divider />
                  </h3>

                  <div slot="body">
                    <div class="row">
                      <div class="col">
                      <v-btn outlined color="#42b983" @click="goService(pick.id)">상세보기</v-btn>
                      </div>
                      <div >
                        <v-radio-group v-model="radio_doing">
                          <v-radio v-for="(n, i) in selects" :key="i" :label="n" :value="i"></v-radio>
                        </v-radio-group>
                      </div>
                    </div>
                  </div>
                  <div slot="footer">
                    <button @click="pickSave(pick, 1, radio_doing)" style="width:33%">저장</button>
                    <button @click="pickDelete(pick, 1)" style="width:33%">삭제</button>
                    <button class="modal-default-button" @click="pick.modal = false; radio_doing=1" style="width:33%">닫기</button>
                  </div>
                </FavoriteModal>
              </div>
            </div>
            <div class="favoritecontents">
              결과나온 정책
              <hr />
              <div class="favoritecontent" v-for="pick in finish_policies" :key="pick.id">
                <div class="font-nanum" style="cursor: pointer;" @click="pick.modal = true">
                  <h4>{{ pick.title }}</h4>
                </div>
                <FavoriteModal v-if="pick.modal" @close="pick.modal = false">
                                <!-- you can use custom content here to overwritedefault content-->
                  <h3 slot="header">
                    {{ pick.title }}
                    <v-divider />
                  </h3>

                  <div slot="body">
                    <div class="row">
                      <div class="col">
                      <v-btn outlined color="#42b983" @click="goService(pick.id)">상세보기</v-btn>
                      </div>
                      <div >
                        <v-radio-group v-model="radio_finish">
                          <v-radio v-for="(n, i) in selects" :key="i" :label="n" :value="i"></v-radio>
                        </v-radio-group>
                      </div>
                    </div>
                  </div>
                  <div slot="footer">
                    <button @click="pickSave(pick, 2, radio_finish)" style="width:33%;">저장</button>
                    <button @click="pickDelete(pick, 2)" style="width:33%;">삭제</button>
                    <button class="modal-default-button" @click="pick.modal = false; radio_finish=2" style="width:33%;">닫기</button>
                  </div>
                </FavoriteModal>
              </div>
            </div>

            <div class="favoritecontents">
              참여 중 채팅방
              <hr />
              <ul v-for="room in mychat" :key="room.id">
                <li style="text-align:left;">
                  <a
                    @click="goService(room.id)"
                    style="text-decoration:none; color:black"
                  >{{room.title}}</a>

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
import FavoriteModal from "./FavoriteModal";
export default {
  name: "PickPage",
  data: () => ({
    mychat: [],
    icons: { del: mdiDelete, chat: mdiChat },
    drawer: null,
    user: null,
    pick_policies: null,
    doing_policies: null,
    finish_policies: null,
    dialog: false,
    selects: ["찜", "진행중", "결과"],
    radio_pick: 0,
    radio_doing: 1,
    radio_finish: 2,
  }),
  components: {
    PolicyChat,
    FavoriteModal
  },
  created() {
    if (localStorage.getItem("token") == null) {
      alert("로그인이 필요합니다.")
      router.push("/login")
    }
    this.getFavoriteData();
  },
  mounted() {
    this.getChatList().then(result => {
      this.mychat = result.data;
    });
  },
  methods: {
    // 으아.. Pick, Doing, Finish 각각 다만들어야됨
    getFavoriteData() {
      this.getPickPolicies()
      this.getDoingPolicies()
      this.getFinishPolicies()
    },
    getPickPolicies() {
      this.$store.dispatch("data/getPickPolicies").then(result => {
        this.pick_policies = result;
      });
    },
    getDoingPolicies() {
      this.$store.dispatch("data/getDoingPolicies").then(result => {
        this.doing_policies = result;
      });
    },
    getFinishPolicies() {
      this.$store.dispatch("data/getFinishPolicies").then(result => {
        this.finish_policies = result;
      });
    },
    pickSave(policy, now, select) {
      if (select != now){
        const params = {
          policyId: policy.id,
          now: now,
          select: select
        }
        if (now == 0){
          this.$store.dispatch("data/editPickPolicies", params).then(response => {
            this.getFavoriteData()
          })

        }
        else if (now == 1){
          this.$store.dispatch("data/editDoingPolicies", params).then(response => {
            this.getFavoriteData()
          })
          
        }
        else{
          this.$store.dispatch("data/editFinishPolicies", params).then(response => {
            this.getFavoriteData()
          })
        }
      }
      this.radio_pick = 0;
      this.radio_doing =  1;
      this.radio_finish = 2;
      policy.modal = false
    },
    pickDelete(policy, now){
      const params = {
          policyId: policy.id,
          now: now
        }
      if (now == 0){
          confirm("Are you sure you want to delete this item?")&&
          this.$store.dispatch("data/deletePickPolicies", params).then(response => {
            this.getFavoriteData()
          })

        }
        else if (now == 1){
          confirm("Are you sure you want to delete this item?")&&
          this.$store.dispatch("data/deleteDoingPolicies", params).then(response => {
            this.getFavoriteData()
          })
          
        }
        else{
          confirm("Are you sure you want to delete this item?")&&
          this.$store.dispatch("data/deleteFinishPolicies", params).then(response => {
            this.getFavoriteData()
          })
        }

      this.radio_pick = 0;
      this.radio_doing =  1;
      this.radio_finish = 2;
      policy.modal = false
    },
    editPickStatus(id) {
      // params에 진행중인지 / 결과나온정책인지 추가

      const params = {
        user: this.$store.state.data.user.username,
        policyId: id
      };
      this.$store.dispatch("data/editPickPolicies", params);
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

  }
};
</script>
<style>
.font-nanum {
  font-family: "Nanum Gothic", sans-serif;
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