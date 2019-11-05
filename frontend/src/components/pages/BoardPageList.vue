<template>
  <v-container class="pa-2" fluid grid-list-md>
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
        <tr v-for="post in ListSliced" pa-2 style="font-family:WONDotum">
          <td class="title">
            <router-link :to="{ name: 'boardDetail', params: {boardId: post.id} }">{{ post.title }}  
              
            </router-link>
            <span style="font-size:small" v-if="post.comments">[{{post.comments}}]</span>
          </td>
          <td class="name">{{post.writer}}</td>
          <td class="date">{{post.when}}</td>
          <td class="hit">{{post.clicked}}</td>
        </tr>
        <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
      </tbody>
    </table>
  </v-container>
</template>


<script>
export default {
  props: {
    getAllBoards: {
      type: Function,
      default: () => {}
    }
  },
  data: () => ({
    boardList: [],
    listPerPage: 10,
    page: 1
  }),

  async mounted() {
    await this.getboard();
  },
  methods: {
    // setLoading() {
    //     if(this.loading){
    //         this.loading = false
    //     }else{
    //         this.loading = true
    //     }
    // },
    async getboard() {
      // await this.setLoading()
      this.boardList = await this.getAllBoards();
      this.boardList = this.boardList.reverse();
      // await this.setLoading()
    }
  },

  computed: {
    // pagination related variables
    ListEmpty: function() {
      return this.boardList.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.boardList.length + this.listPerPage - 1) / this.listPerPage
      );
    },
    ListSliced: function() {
      return this.boardList.slice(
        this.listPerPage * (this.page - 1),
        this.listPerPage * this.page
      );
    }
  }
};
// export default {
//   props: {
// id: {
//   type: Number,
//   default: 0
// },
//     title: {
//       type: String,
//       default: ""
//     },
//     content: {
//       type: String,
//       default: ""
//     },
//   },
//   computed: {
// genresStr: function() {
//   return this.genres.join(" / ");
// },
//   }
// };
</script>

<style>
@font-face {
  font-family: "WONDotum";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/WONDotum.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
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