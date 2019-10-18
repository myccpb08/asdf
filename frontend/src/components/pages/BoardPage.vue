<template>
  <div>
    <!-- <v-card class="mx-auto">
      <v-toolbar color="pink" dark>
        <v-toolbar-title>자유게시판</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <br>
      <v-container fluid grid-list-md pa-2>
    <v-layout wrap style="width:80%; margin-left:10%;">-->

    <!-- 공지사항 형식 -->
    <template>
      <v-container class="mt-3 ml-5">
        <!-- 리스트 게시판 시작-->
        <div class="row">
          <div class="span_10">
            <h1>자유게시판</h1>
          </div>
          <div class="span_2" style="text-align:right;">
             <router-link to='/board/write' style="text-decoration:none;">  
            <v-btn class="ma-2" tile outlined color="success">
              <v-icon left>mdi-pencil</v-icon>Edit
            </v-btn>
             </router-link>
          </div>
        </div>
        <br />

        <table class="sub_news" border="2" cellspacing="0">
          <colgroup>
            <col />
            <col width="110" />
            <col width="100" />
            <col width="80" />
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
            <tr>
              <td class="title">
                <a href="#">본문</a>
                <!-- <img width="13" height="12" class="pic" alt="첨부이미지" src="첨부파일 ic_pic.gif"> <a class="comment" href="#">[5]</a>
                <img width="10" height="9" class="new" alt="새글" src="첨부파일/ic_new.gif">-->
              </td>
              <td class="name">본문작성</td>
              <td class="date">2019/10/18</td>
              <td class="hit">1234</td>
            </tr>

            <tr class="reply">
              <td class="title" style="padding-left:30px;">
                <a href="#">본문답글</a>
              </td>
              <td class="name">본문답글</td>
              <td class="date">2019/10/18</td>
              <td class="hit">1234</td>
            </tr>

            <!-- tr이 제목 1줄입니다 보일 list 갯수만큼 li반복합니다.-->
          </tbody>
        </table>

        <!-- 리스트 게시판 끝-->
      </v-container>
    </template>
  </div>
</template>




<!-- 공지사항 끝 -->














          <!-- <v-flex style="text-align:center; width:100%;" v-for="i in totalletters">
            <div color="white" style="min-height:110px; width:100%; border: 4px solid gray;">
                {{ i }} -->


              <!-- <v-btn @click='openmodal(i.favorite)' style="width:80%; box-shadow:none; min-height:110px; backgroundColor:white">
                <v-img aspect-ratio=1 :src='i.favorite.logo' contain style="width:10%; margin-left:5%; "></v-img>
                <div style="width:80%; ">
                  {{i.favorite.name}}<br>
                  <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-if="i.favorite.end===undefined">채용시 마감</p>
                  <p style="font-size:17px; color:gray; padding-left:20px; overflow:auto;" v-else>{{i.favorite.start}} ~ {{i.favorite.end}}
                  </p>
                </div>
              </v-btn> -->
              <!-- <v-btn icon @click='delfavorite(i.favorite)'>
                <v-icon color="red" style="width:5%;">delete</v-icon>
              </v-btn> -->
            <!-- </div>
            <br>
          </v-flex>
        </v-layout>
      </v-container>
      <br>
    </v-card> -->

    </div>
</template>

<script>
export default {
  data: () => ({
    totalletters: ["글1", "글2", "글3"]
  })
};
</script>


<style>
/* .container {
          margin: 2%;
          padding: 0;
        } */
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
/* .sub_news tr.reply .title a{padding-left:16px;background:url(첨부파일/ic_reply.png) 0 1px no-repeat} */
/* //게시판 리스트 목록 */
</style>