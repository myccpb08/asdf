<template>
  <div>
    <!-- <div style="margin-top:108px"></div> -->
        <div class="test">
          <h2>글쓰기</h2>
          <BoardWriteForm :submit="boardWrite"></BoardWriteForm>

      </div>
    <!-- <div style="margin-top:78px"></div> -->
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import BoardWriteForm from './BoardWriteForm'


export default {
  name: 'BoardWriter',
    components: {
    BoardWriteForm
  },
  data: () => ({}),
  // computed: {
  //   ...mapState({
  //     movieList: state => state.data.movieSearchList
  //   })
  // },
  methods: mapActions("data", ["boardWrite"])

//   methods:{
//     async postBoard(title, body, img){
//       if(title == ''){
//         alert("제목을 입력해주세요")
//       }else if(body == ''){
//         alert("내용을 입력해주세요")
//       }else{
//         await FirebaseService.postBoard(title, body, img, this.$store.state.user)
//         alert("Board가 작성되었습니다.")
//         this.$router.replace('/board')
//       }
//     }
//   }
}
</script>

<style>
/* .container {
          margin: 2%;
          padding: 0;
        } */
.test {
  overflow: hidden;
  width: 60%;
  margin: auto;
  margin-top: 3%;
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

</style>