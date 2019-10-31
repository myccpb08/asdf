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

                  <div style='text-align:right'>
                    <div>작성일 : {{board.when}}</div>
                    <div>작성자 : {{board.writer}}</div>
                    <div>이메일 : {{board.email}}</div>
                    <div>조회수 : {{board.clicked+1}}</div>
                  </div>
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
                <!-- 댓글이 없고, 로그인 하지 않았으면 -->
                <div v-if="this.check == false && this.commentsgroup.length == 0">로그인 후 첫 댓글을 남겨주세요.</div>
                <div v-if="this.check == true && this.commentsgroup.length == 0">첫 댓글을 남겨보세요</div>
                <div v-else>
                  <div v-for="comment in commentsgroup" v-bind:key="comment.id">
                    <div v-if="!comment.edit" style="min-height:40px">
                      {{comment.writer}} - {{comment.content}}
                      
                      <!-- 댓글수정버튼 -->
                      
                      <v-btn x-small v-if="check == true && comment.email == $store.state.data.user.username" class="ma-0" text icon @click="comment.edit = !comment.edit">
                        <v-icon color="blue">{{icons.edit}}</v-icon>
                      </v-btn>
                      
                      <!-- 댓글삭제버튼 -->
                      <v-btn x-small v-if="check == true && comment.email == $store.state.data.user.username" @click="deleteComment(comment.id)" class="ma-1" text icon>
                        <v-icon color="red">{{icons.del}}</v-icon>
                      </v-btn>
                    </div>

                    <!-- 댓글 수정 폼 -->
                    <form v-if="comment.edit">
                      <v-text-field
                        v-model="comment.content"
                        placeholder="comment.content"
                        :append-icon="icons.editsubmit"
                        @click:append="editCommentContents(boardId, comment.content, comment.id)"
                      ></v-text-field>
                    </form>
                  </div>
                </div>

                <!-- 댓글 작성 폼 -->
                <div v-if="this.check == true">
                <BoardCommentForm :Id="boardId" :submit="boardCommentWrite" />
                </div>
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
import { mdiPencil, mdiDelete, mdiCheck } from "@mdi/js";
import BoardCommentForm from "./BoardCommentForm";
import { mapState, mapActions } from "vuex";

export default {
  name: "BoardDetail",
  data() {
    return {
      boardId: this.$route.params.boardId,
      board: {},
      clicked : '',
      content: "",
      update_content: "",
      check: false,
      commentsgroup: {},
      icons: { edit: mdiPencil, del: mdiDelete, editsubmit: mdiCheck },
      user : this.$store.state.data.user
    };
  },
  components: { BoardCommentForm },

  mounted() {
    this.logincheck()

    this.getBoard(this.boardId).then(result => {
      this.board = result;
      this.board.id = this.boardId;
      this.clicked = result.clicked
      this.changeClicked(this.boardId)

    });

    this.getComments(this.boardId).then(result => {
      this.commentsgroup = result;
    });

  
  },

  methods: {
    ...mapActions("data", ["boardCommentWrite"]),

    async logincheck(){
      if (localStorage.getItem("token") !== undefined && localStorage.getItem("token") !== null){
        this.check = true
      }
    },

    async getBoard(id) {
      return this.$store.dispatch("data/getBoardDetail", id);
    },

    async changeClicked(){
       const params = {
        clicked : this.clicked + 1,
        id : this.boardId
      };
        this.$store.dispatch("data/boardUpdate", params)
    },

    
    async deleteBoard() {
      console.log(this.boardId)
      this.$store.dispatch("data/deleteBoard", this.boardId);
      this.$router.go(-1);
    },

    async getComments(id) {
      /* 해당 글 id 로 글을 조회해서, 거기에 달린 댓글을 가져와야 함 */
      return this.$store.dispatch(
        "data/getBoardComments",
        id
      );
    },

    async deleteComment(id) {
      this.$store.dispatch("data/deleteBoardComment", id);
      window.location.reload();
    },

    async editCommentContents(boardId, content, commentId){
      const params = {
        boardId : boardId,
        content : content,
        commentId : commentId
      }
      this.$store.dispatch("data/editBoardComment", params);
      this.getComments(boardId)
      window.location.reload()
    }
  }
};
</script>
