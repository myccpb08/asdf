<template>
  <div>
    <v-card class="mx-auto">
      <v-toolbar color="lightgray" white>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title>
          <img src="../../images/glass_row.png" class="header_left" />
        </v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <br />
      <v-container fluid grid-list-md pa-2>
        <v-layout style="margin-left:10%;">
          <div class="pickbox">
            <!-- <v-flex class="pickbox" v-for="i in totalpick"> -->
            <div class="pickcontents">
              찜 해놓은 정책
              <hr />
              <div class="pickcontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="pickcontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="pickcontent">
                <h4>청년내일채움공제</h4>
              </div>
              <div class="pickcontent">
                <h4>청년내일채움공제</h4>
              </div>
            </div>
            <div class="pickcontents">
              진행중인 정책
              <hr />
              <div class="pickcontent">
                <h4>내집마련 정책</h4>
              </div>
              <div class="pickcontent">
                <h4>내집마련 정책</h4>
              </div>
              <div class="pickcontent">
                <h4>내집마련 정책</h4>
              </div>
            </div>
            <div class="pickcontents">
              결과나온 정책
              <hr />
              <div class="pickcontent">
                <h4>한 부모 가정 지원</h4>
              </div>
            </div>
            <!-- <div class="pickcontent" color="white">
                  
                  
                  {{ i }}
                <v-btn @click='openmodal(i.pick)' style="width:80%; box-shadow:none; min-height:110px; backgroundColor:white">
                  <v-img aspect-ratio=1 :src='i.pick.logo' contain style="width:10%; margin-left:5%; "></v-img>
                  <div style="width:80%; ">
                    {{i.pick.name}}<br>
                    <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-if="i.pick.end===undefined">채용시 마감</p>
                    <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-else>{{i.pick.start}} ~ {{i.pick.end}}
                    </p>
                  </div>
                </v-btn>
                <v-btn icon @click='delpick(i.pick)'>
                  <v-icon color="red" style="width:5%;">delete</v-icon>
                </v-btn>
              </div>
            <br>
            </v-flex>-->
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
export default {
  name: "PickPage",
  data: () => ({
    
  })
};
</script>
<style>
.header_left {
  width: 17%;
}
.pickbox {
  display: flex;
  text-align: center;
  width: 33.3%;
  min-width: 100%;
  min-height: 400px;
}
.pickcontents {
  margin: 2%;
  padding: 2%;
  border-radius: 7px;
  min-height: 110px;
  width: 100%;
  border: 4px solid rgb(187, 187, 187);
  text-align: center;
}
.pickcontent {
  margin: 2%;
  padding: 1%;
  border-radius: 7px;
  width: 40%;
  border: 1px solid gray;
  text-align: center;
  display: inline-flex;
}
</style>