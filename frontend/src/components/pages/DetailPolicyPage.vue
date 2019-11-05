<template>
  <v-container class="pa-2" fluid grid-list-md style="width:80%;">
        <div class="line" style="width:70%; ">
            <div class="detail">
                <div class="detailrow_icon">
                    <img src="../../images/All_view.png" alt="" style="width: 70%;">
                </div>
                <div class="detailrow">
                    <h2>한 눈에 보는 복지정보</h2>
                    <h4>다양한 복지서비스 정보를 안내해드립니다.</h4>
                </div>
                
            </div>
        </div>

        <div class="additional">
                  <span<strong>조회수 {{policy.clicked+1}}</strong></span>

                    <!-- 채팅 버튼 -->
                    <!-- <v-btn text @click.stop="drawer = !drawer"> -->
                    <v-btn text @click ="this.test">
                      <v-icon large color="warning">{{icons.chat}}</v-icon>
                    </v-btn>

                    <button style="color:	#FFD700;" @click="toggleMyPick">
                      <i v-if="is_myPick" class="fas fa-star fa-lg"></i>
                      <i v-else class="far fa-star fa-lg"></i>
                    </button>
            </div>

            <!-- 채팅 drawer 시작 -->
            <v-navigation-drawer v-model="drawer" absolute temporary right width=350 >
              <v-list-item>
                <v-list-item-avatar>
                  <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>{{policy.title}}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <PolicyChat :Id="policyId"></PolicyChat>
            </v-navigation-drawer>
      <!-- 채팅 drawer 끝 -->


        <div class="line">
            <div style="border-top: 2px solid orange; height: 10px; width: 100%;"></div>
            <div style="border: 1px solid rgb(187, 187, 187); min-height:110px;" class="textrow">
                <strong class="head" style="text-align: center;">
                    <h2>{{policy.title}}</h2>
                </strong>
                <strong class="head" style="text-align: center;">
                    <h4>{{policy.brief}}</h4>
                </strong>
            </div>
        </div>
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
                  <img src="../../images/Eligibility.png" alt="" style="width: 70%;">
                </div>
                <div class="detailrow">
                    <h2>누가 받을 수 있나요?</h2>
                </div>
            </div>
            
        </div>
        <!-- <div style="border-top: 2px solid orange; height: 10px; width: 100%;"></div> -->
        <div class="line">
            <div class="textrow" style="border: 1px solid rgb(187, 187, 187); min-height:110px; border-top: 2px solid orange; border-bottom: 2px solid orange;">
                <strong class="head">
                    <strong class="head">
                        <h2>지원대상</h2>
                    </strong>
                </strong>
                <strong class="head">
                  <ul>
                    <li v-for="pol in policy.target">
                      <span style="font-size:large;">{{pol.content}}</span>
                      <ul>
                        <li v-for="po in pol.body">
                          {{po.content}}
                          <ul>
                            <li v-for="p in po.body">
                              {{p.content}}
                            </li>
                          </ul>
                        </li>
                      </ul>
                      <br>
                    </li>
                  </ul>
                </strong>

                <strong class="head"  v-if="policy.criteria">
                    <strong class="head">
                        <h2>선정기준</h2>
                    </strong>
                </strong>
                <strong class="head" v-if="policy.criteria">
                    <ul>
                    <li v-for="pol in policy.criteria">
                      <span style="font-size:large;">{{pol.content}}</span>
                      <ul>
                        <li v-for="po in pol.body">
                          {{po.content}}
                          <ul>
                            <li v-for="p in po.body">
                              {{p.content}}
                            </li>
                          </ul>
                        </li>
                      </ul>
                      <br>
                    </li>
                  </ul>
                </strong>
            </div>
        </div>
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
                  <img src="../../images/Benefits.png" alt="" style="width: 70%;">
                </div>
                <div class="detailrow textrow">
                    <h2>어떤 혜택을 받을 수 있나요?</h2>
                </div>
            </div>
        </div>
        <div class="line">
            <!-- <div style="border-top: 2px solid orange; height: 10px; width: 100%;"></div> -->
            <div class="textrow" style="border: 1px solid rgb(187, 187, 187); min-height:110px; border-top: 2px solid orange; border-bottom: 2px solid orange;">
                <strong class="head">
                    <h2>지원내용</h2>
                </strong>
                <strong class="head">
                  <ul>
                    <li v-for=" pol in policy.content" >
                      <span style="font-size:large;">{{pol.content}}</span>
                      <ul>
                        <li v-for="po in pol.body">
                          {{po.content}}
                          <ul>
                            <li v-for="p in po.body">
                              {{p.content}}
                            </li>
                          </ul>
                        </li>
                      </ul>
                      <br>
                    </li>
                  </ul>
                </strong>
            </div>
        </div>
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
                  <img src="../../images/Apply.png" alt="" style="width: 70%;">
                </div>
                <div class="detailrow">
                    <h2>어떻게 신청하나요?</h2>
                </div>
            </div>
        </div>
        <div class="line">
            <div class="textrow" style="border: 1px solid rgb(187, 187, 187); min-height:110px; border-top: 2px solid orange; border-bottom: 2px solid orange;">
            <strong class="head" v-if="policy.supply_way">
                <h2>신청방법</h2>
            </strong>
            <strong class="head" v-if="policy.supply_way">
              <ul>
                    <li v-for="pol in policy.supply_way">
                      <span style="font-size:large;">{{pol.content}}</span>
                      <ul>
                        <li v-for="po in pol.body">
                          {{po.content}}
                          <ul>
                            <li v-for="p in po.body">
                              {{p.content}}
                            </li>
                          </ul>
                        </li>
                      </ul>
                      <br>
                    </li>
                  </ul>
            </strong>

            <strong class="head" v-if="policy.procedure">
                <h2>지원절차</h2>
            </strong>
            <strong class="head" v-if="policy.procedure" style="width:100%; text-align:center;">
                <div  v-for="(pol, i) in policy.procedure">
                  <div v-if="i>0" class="procedureImg">
                    <div></div>
                    <div><img src="../../images/Arrow.png" alt="" style="width:100%;"></div>
                    <div></div>
                  </div>
                  <div class="procedureDiv">
                    <div >{{pol.content}}</div><hr>
                    <div>{{pol.body[0].content}}</div>
                  </div>
                </div>
            </strong>
                
            </div>
        </div>
        <div class="line" v-if="policy.site">
            <div class="detail">
                <div class="detailrow_icon">
                  <img src="../../images/Questions.png" alt="" style="width: 70%;">
                </div>
                <div class="detailrow">
                     <h2>아직 궁금한 것이 있어요!</h2>
                </div>
            </div>
        </div>
        <div class="line" v-if="policy.site">
            <div class="textrow" style="border: 1px solid rgb(187, 187, 187); min-height:110px; border-top: 2px solid orange; border-bottom: 2px solid orange;">
                <strong class="head"> 
                    <h2>사이트</h2>
                </strong>
                
                <ul>
                  <li>
                    {{policy.site[0]}} : <a v-bind:href=policy.site[1]> {{policy.site[1]}} </a>
                  </li>
                </ul>
                
            </div>
        </div>
    </v-container>
</template>


<script>
import store from "../../store/modules/data.js";
import { mapState, mapActions } from "vuex";
import router from "../../router/index.js";
import { mdiChatProcessing, mdiChat, mdiDelete } from "@mdi/js";
import PolicyChat from './PolicyChat'

export default {
  data() {
    return {
      policyId: this.$route.params.policyId,
      policy : {},
      is_myPick: false,
      icons: { chat: mdiChat },
      drawer: null
    };
  },

  components :{
    PolicyChat
  },

  async mounted() {
    await this.getService(this.policyId).then(result => {
      this.policy = result;
      console.log(this.policy);
      this.saveLatestView()
    });
    this.$store.dispatch("data/getUser").then(response => {

            this.is_myPick = response['pick_policies'].some(pick_policy=> {
              return pick_policy == this.policyId
            }) || 
            response['doing_policies'].some(pick_policy=> {
              return pick_policy == this.policyId
            }) ||
            response['finish_policies'].some(pick_policy=> {
              return pick_policy == this.policyId
            })
          })
    // console.log(this.$store.state.data.user)
    // let vm = this
    // // pick 정책중에 현재 정책이 포함되어 있으면 true
    // this.is_myPick = this.$store.state.data.user.pick_policies.some(function(pick_policy){
    //   return pick_policy == vm.policyId
    // })
  },
  methods: {

    async test(event){
      this.drawer = !this.drawer
      event.stopPropagation()
      return this.$store.dispatch('data/myChat', this.policyId)

    },

    async getService(policyId) {
      return this.$store.dispatch(
        "data/getService",
        policyId
      )
    },
    saveLatestView(){
      console.log("hihihi : " + this.policy.id)
      const params = {
        username : this.$store.state.data.user.username,
        path : this.policy.id
      }
      console.log(params)
      this.updateLatestView(params)
    },
    ...mapActions("data", ["updateLatestView"]),
    toggleMyPick(){
      
      const params = {
        id: this.policyId,
        user: this.$store.state.data.user.username
      };
    
      if ( this.$store.dispatch("data/getUser").then(response => {
            response['doing_policies'].some(pick_policy=> {
                return pick_policy == this.policyId
            }) ||
            response['finish_policies'].some(pick_policy=> {
              return pick_policy == this.policyId
            }) 
            }) ) {
            alert('딱정함에서 제거해주세요')
          }
      else {
        this.is_myPick = !this.is_myPick;
        this.$store.dispatch("data/editServicePick", params).then((result) => {
          this.$store.dispatch("data/editSession", localStorage.getItem('token'))
      });
      }
    },
  }
};
</script>

<style>
.detail {
  width: 100%;
  height: 100%;
  display: table-row;
}
.detailrow_icon {
  padding-left: 5%;
  display: table-cell;
  width: 130px;
}
.detailrow {
  float: left;
  width: 87%;
  min-width: 500px;
}
.additional{
  float: right;
  width:20%;
  text-align:right;
}
.line {
  padding-top: 3%;
}
.head {
  padding: 7%;
}
.textrow {
  padding-left: 3%;
  padding-right: 3%;
  /* 한 줄 자르기 */
  display: inline-block;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;

  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal;
  line-height: 1.2;
  text-align: left;
}
li {
  text-indent: inherit;
}
.row {
  overflow: hidden;
  width: 100%;
}
.row [class*="span"] {
  float: left;
  margin-left: 2%;
}
.row [class*="span"]:first-child {
  margin-left: 0;
}
.span_1 {
  width: 6.5%;
  *width: 6%;
}
.span_2 {
  width: 15%;
  *width: 14.5%;
}
.span_3 {
  width: 23.5%;
  *width: 23%;
}
.span_4 {
  width: 32%;
  *width: 31.5%;
}
.span_5 {
  width: 40.5%;
  *width: 40%;
}
.span_6 {
  width: 49%;
  *width: 48.5%;
}
.span_7 {
  width: 57.5%;
  *width: 57%;
}
.span_8 {
  width: 66%;
  *width: 65.5%;
}
.span_9 {
  width: 74.5%;
  *width: 74%;
}
.span_10 {
  width: 83%;
  *width: 82.5%;
}
.span_11 {
  width: 91.5%;
  *width: 91%;
}
.span_12 {
  width: 100%;
  *width: 99.5%;
}

/* 게시판 리스트 목록 */
.sub_news,
.sub_news th,
.sub_news td {
  border: 0;
}
.sub_news a {
  color: #383838;
  text-decoration: none;
}
.sub_news {
  width: 100%;
  border-bottom: 1px solid #999;
  color: #666;
  font-size: 12px;
  table-layout: fixed;
}
.sub_news caption {
  display: none;
}
.sub_news th {
  padding: 5px 0 6px;
  border-top: solid 1px #999;
  border-bottom: solid 1px #b2b2b2;
  background-color: #f1f1f4;
  color: #333;
  font-weight: bold;
  line-height: 20px;
  vertical-align: top;
}
.sub_news td {
  padding: 8px 0 9px;
  border-bottom: solid 1px #d2d2d2;
  text-align: center;
  line-height: 18px;
}
.sub_news .date,
.sub_news .hit {
  padding: 0;
  font-family: Tahoma;
  font-size: 11px;
  line-height: normal;
}
.sub_news .title {
  text-align: left;
  padding-left: 15px;
  font-size: 13px;
}
.sub_news .title .pic,
.sub_news .title .new {
  margin: 0 0 2px;
  vertical-align: middle;
}
.sub_news .title a.comment {
  padding: 0;
  background: none;
  color: #f00;
  font-size: 12px;
  font-weight: bold;
}

ul li { 
  line-height:160%;
  font-weight: 400 ;
}

.procedureDiv{
    width:18%;
    height: 160px;
    border: 1px solid gray;
    border-radius: 7px;
    float: left;
    background-color:
}

.procedureDiv div{
    padding: 1vh;
}

.procedureImg{
  height: 160px;
  margin-left:1%;
  margin-right:1%;
  margin-bottom:2%;
  width: 5%;
  float: left;
}

.procedureImg div{
  height: 33%;
}


</style>