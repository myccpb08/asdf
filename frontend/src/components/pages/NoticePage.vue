<template>
  <v-container>
    <!-- 리스트 게시판 시작-->
    <div>
        <h1>공지사항</h1>
    </div>
    <br>

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



<style>
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
