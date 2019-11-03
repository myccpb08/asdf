<template>
  <v-container class="pa-2" fluid grid-list-md style="width:80%;">
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
                    <!-- <img src="../../images/All_view.png" alt="" style="width: 70%;">-->
                </div>
                <div class="detailrow">
                    <h2>한 눈에 보는 복지정보</h2>
                    <h4>다양한 복지서비스 정보를 안내해드립니다.</h4>
                </div>
            </div>
            ``
        </div>
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
                  <!--  <img src="../../images/Eligibility.png" alt="" style="width: 70%;">-->
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
                        <h4>{{policy.target}}</h4>
                </strong>

                <strong class="head">
                    <strong class="head">
                        <h2>선정기준</h2>
                    </strong>
                </strong>
                <strong class="head">
                    <li>
                        {{policy.criteria}}
                    </li>
                </strong>
            </div>
        </div>
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
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
                    <h4>{{policy.content}}</h4>
                </strong>
            </div>
        </div>
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
                </div>
                <div class="detailrow">
                    <h2>어떻게 신청하나요?</h2>
                </div>
            </div>
        </div>
        <div class="line">
            <div class="textrow" style="border: 1px solid rgb(187, 187, 187); min-height:110px; border-top: 2px solid orange; border-bottom: 2px solid orange;">
            <strong class="head">
                <h2>신청방법</h2>
            </strong>
            <strong class="head">    
                <h4>{{policy.supply_way}}</h4>
            </strong>

            <strong class="head">
                <h2>지원절차</h2>
            </strong>
            <strong class="head"> 
                <h4>
                    다음과 같은 순서로 지원합니다
                </h4>
            </strong>
            <strong class="head">    
                <h4>{{policy.procedure}}</h4>
            </strong>
                
            </div>
        </div>
        <div class="line">
            <div class="detail">
                <div class="detailrow_icon">
                </div>
                <div class="detailrow">
                     <h2>아직 궁금한 것이 있어요!</h2>
                </div>
            </div>
        </div>
        <div class="line">
            <div class="textrow" style="border: 1px solid rgb(187, 187, 187); min-height:110px; border-top: 2px solid orange; border-bottom: 2px solid orange;">
                <strong class="head"> 
                    <h2>사이트</h2>
                </strong>
                
                <h4>
                    {{policy.site}}
                </h4>
            </div>
        </div>
        <div class="line">
            <table class="sub_news" border="2" cellspacing="0">
                <colgroup>
                    <col />
                    <col width="9%" />
                    <col width="8%" />
                    <col width="7%" />
                </colgroup>
                <thead>
                    <tr>
                    <th scope="col">제목</th>
                    <th scope="col">글쓴이</th>
                    <th scope="col">날짜</th>
                    <th scope="col">조회수</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="post in ListSliced" pa-2>
                        <td class="title">
                            <router-link
                            :to="{ name: 'boardDetail', params: {boardId: post.id} }"
                            >{{ post.title }}</router-link>
                        </td>
                        <td class="name">{{post.content}}</td>
                        <td class="date">2019/10/18</td>
                        <td class="hit">1234</td>
                    </tr>
                    <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
                </tbody>
            </table>
        </div>
    </v-container>
</template>


<script>
import store from "../../store/modules/data.js";
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      policyId: this.$route.params.policyId,
      policy : {}
    };
  },

  async mounted() {
    this.getService(this.policyId).then(result => {
      this.policy = result;
      console.log(this.policy);
      this.saveLatestView()
    })
  },
  methods: {
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
    ...mapActions("data", ["updateLatestView"])
  }
};
</script>

<style>
.detail {
    width: 100%;
    height: 100%;
    display:table-row;
}
.detailrow_icon {
    padding-left: 5%;
    display:table-cell;
    width: 130px;
}
.detailrow {
    float:left;
    width: 87%;
    min-width: 500px;
}
.line {
    padding-top: 3%;
}
.head {
    padding: 7%
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
</style>