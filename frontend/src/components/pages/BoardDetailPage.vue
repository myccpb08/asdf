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
              </v-flex>
              <v-flex xs12 text-xs-center round my-5>
                <v-btn
                  :to="{ name: 'boardUpdate', params: {boardId: this.boardId} }"
                  color="gray"
                  class="movebtn"
                >update</v-btn>
                <v-btn color="gray" @click="deleteBoard()" class="movebtn">delete</v-btn>
                <v-btn color="gray" @click="$router.go(-1)" class="movebtn">back</v-btn>
              </v-flex>

              <!-- 댓글영역 -->
              <div>
                <div v-if="this.commentsgroup.length == 0">첫 댓글을 남겨보세요</div>
                <div v-else>
                  <div v-for="comment in commentsgroup" v-bind:key="comment.id">
                    {{comment.user}} - {{comment.content}}
                    <!-- 댓글수정버튼 -->
                    <v-btn class="ma-1" text icon>
                      <v-icon color="blue">{{icons.edit}}</v-icon>
                    </v-btn>
                    <!-- 댓글삭제버튼 -->
                    <v-btn @click="deleteComment(comment.id)" class="ma-1" text icon>
                      <v-icon color="red">{{icons.del}}</v-icon>
                    </v-btn>
                  </div>
                </div>

                <!-- 댓글 작성 폼 -->
                <BoardCommentForm :Id="boardId" :submit="boardCommentWrite"/>

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
import { mdiPencil, mdiDelete } from "@mdi/js";
import BoardCommentForm from "./BoardCommentForm"
import { mapState, mapActions } from "vuex";

export default {
  name: "BoardDetail",
  data() {
    return {
      boardId: this.$route.params.boardId,
      board: {},
      content: "",
      update_content: "",
      check: false,
      commentsgroup: {},
      icons: { edit: mdiPencil, del: mdiDelete }
    };
  },
  components: {BoardCommentForm},
  mounted() {
    this.getBoard(this.boardId).then(result => {
      this.board = result;
      this.board.id = this.boardId;
    });

    this.getComments(this.boardId).then(result => {
      this.commentsgroup = result;
    });
  },
  methods: {
    ...mapActions("data", ["boardCommentWrite"]),

    async getBoard(id) {
      return this.$store.dispatch("data/getboarddetail", id);
    },
    async deleteBoard() {
      this.$store.dispatch("data/DeleteBoard", this.boardId);
      this.$router.go(-1);
    },

    async getComments(id) {
      /* 해당 글 id 로 글을 조회해서, 거기에 달린 댓글을 가져와야 함 */
      return this.$store.dispatch(
        "data/getBoardComments",
        id
      ); /* 반환값 = 해당 글의 댓글 전체 */
    },

    async deleteComment(id){
      this.$store.dispatch("data/deleteBoardComment", id)
      window.location.reload()
    }
  }
};
</script>
