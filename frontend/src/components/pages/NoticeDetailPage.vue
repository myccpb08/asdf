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
                  <br />
                  <div style="min-width:20px; text-align:center;">
                    <strong
                      class="display-1"
                      style="display:inline-block; margin-top: 15px;"
                    >{{board.title}}</strong>
                    <br />
                    <div style="height:1px; width:100%; background:lightgray;"></div>
                  </div>

                  <!-- <div style='text-align:right'>
                    <div>작성일 : {{formatedDate(notice.created_at)}}</div>
                    <div>작성자 {{notice.displayName}} | {{notice.email}}</div>
                  </div>-->
                  <br />
                  {{board.content}}
                </div>
                <hr />
              </v-flex>
              <v-flex xs12 text-xs-center round my-5>
                <v-btn
                  :to="{ name: 'noticeUpdate', params: {boardId: board.id} }"
                  color="warning"
                >update</v-btn>
                <v-btn color="cyan" @click="deleteNotice()">delete</v-btn>
                <v-btn color="purple" @click="$router.go(-1)">back</v-btn>
              </v-flex>

              <!-- 댓글영역 -->
              <div>
                <div v-if="this.commentsgroup.length == 0">첫 댓글을 남겨보세요</div>
                <div v-else>
                  <div v-for="comment in commentsgroup" v-bind:key="comment.id">
                    <div v-if="!comment.edit">
                    {{comment.user}} - {{comment.content}}
                    <!-- 댓글수정버튼 -->
                    <v-btn class="ma-1" text icon @click="comment.edit = !comment.edit">
                      <v-icon color="blue">{{icons.edit}}</v-icon>
                    </v-btn>
                    <!-- 댓글삭제버튼 -->
                    <v-btn @click="deleteComment(comment.id)" class="ma-1" text icon>
                      <v-icon color="red">{{icons.del}}</v-icon>
                    </v-btn>
                  </div>
                      <!-- 댓글 수정 폼 -->
                    <form v-if="comment.edit">
                      <v-text-field
                        v-model="comment.content"
                        placeholder="comment.content"
                        :append-icon="icons.editsubmit"
                        @click:append="editCommentContents(noticeId, comment.content, comment.id)"
                      ></v-text-field>
                    </form>


                </div>
                </div>

                <!-- 댓글 작성 폼 -->
                <NoticeCommentForm :Id="noticeId" :submit="noticeCommentWrite"/>


              </div>
              <!-- 댓글 끝 -->

            </v-layout>

            <hr />
          </div>
        </v-flex>
      </v-card>
    </v-container>
    <br />
    <br />
    <br />
  </div>
</template>

<script>
import store from "../../store/modules/data.js";
import {mdiPencil,mdiDelete,mdiCheck} from '@mdi/js';
import NoticeCommentForm from "./NoticeCommentForm"
import { mapState, mapActions } from "vuex";

export default {
  name: "NoticeDetail",
  data() {
    return {
      noticeId: this.$route.params.noticeId,
      board: {},
      content: "",
      update_content: "",
      check: false,
      commentsgroup: {},
      icons : {'edit': mdiPencil, 'del':mdiDelete, editsubmit: mdiCheck}
    };
  },
  components: {NoticeCommentForm},
  mounted() {
    this.getNotice(this.noticeId).then(result => {
      this.board = result;
    });

    this.getComments(this.noticeId).then(result => {
      this.commentsgroup = result;
    });
  },
  methods: {
    ...mapActions("data", ["noticeCommentWrite"]),

    async getNotice(id) {
      return this.$store.dispatch("data/getNoticeDetail", id);
    },
    async deleteNotice() {
      this.$store.dispatch("data/DeleteNotice", this.noticeId);
      this.$router.go(-1);
    },

    async getComments(id) {
      /* 해당 글 id 로 글을 조회해서, 거기에 달린 댓글을 가져와야 함 */
      return this.$store.dispatch(
        "data/getNoticeComments",
        id
      ); /* 반환값 = 해당 글의 댓글 전체 */
    },

    
    async deleteComment(id){
      this.$store.dispatch("data/deleteNoticeComment", id)
      window.location.reload()
    },

        async editCommentContents(noticeId, content, commentId){
          console.log(22222)
      const params = {
        noticeId : noticeId,
        content : content,
        commentId : commentId
      }
      this.$store.dispatch("data/editNoticeComment", params);
      this.getComments(noticeId)
      window.location.reload()
    }
  }
};
</script>
