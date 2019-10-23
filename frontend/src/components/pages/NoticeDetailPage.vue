<template>
  <div>
    <div style="margin-top:68px"></div>
    <v-container>
      <v-card>
        <v-flex xs8 offset-xs2>
          <div>
            <v-layout column>
              <v-flex xs12>
                <div>
                <br>
                  <div style='min-width:20px; text-align:center;'>
                    <strong class="display-1" style="display:inline-block; margin-top: 15px;">{{board.title}}</strong>
                    <br>
                    <div style="height:1px; width:100%; background:lightgray;"></div>
                  </div>

                  <!-- <div style='text-align:right'>
                    <div>작성일 : {{formatedDate(notice.created_at)}}</div>
                    <div>작성자 {{notice.displayName}} | {{notice.email}}</div>
                  </div> -->
                  <br>
                  {{board.content}}
                </div>
              </v-flex>
              <v-flex  xs12 text-xs-center round my-5>
                <v-btn :to="{ name: 'noticeUpdate', params: {boardId: board.id} }" color="gray" class="movebtn">update</v-btn>
                <v-btn color="gray" @click='deleteNotice()' class="movebtn">delete</v-btn>
                <v-btn color="gray" @click='$router.go(-1)' class="movebtn">back</v-btn>
              </v-flex>
            </v-layout>
            <hr>
          </div>
        </v-flex>
      </v-card>
    </v-container>
    <br><br><br>
  </div>
</template>

<script>
import store from "../../store/modules/data.js";

export default {
  name: 'NoticeDetail',
  data(){
    return{
      noticeId: this.$route.params.noticeId,
      board :{},
      content: '',
      update_content: '',
      check:false
    }
  },
   components: {
   },
  mounted(){
    this.getNotice(this.noticeId).then((result) => {
      this.board = result
    })
  },
  methods:{

    async getNotice(id) {
        console.log('여기는 Notice_Detail_Page.vue')
        return this.$store.dispatch("data/getnoticedetail", id)
    },
    async deleteNotice(){
        this.$store.dispatch("data/DeleteNotice", this.noticeId)
        this.$router.go(-1);
    },
  },
}
</script>
