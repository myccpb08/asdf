<template>
  <v-container>
    <v-layout>
      <v-flex style="display: flex; align-items: center; justify-content: center;">
        <div style="width:400px;">
          <!-- <template v-if="uid"> -->
          <template>
            <div id="_chat">
              <div v-for="v in chat" class="_chat" :class="{_right: (v.email == email)}">
                <div class="_msg" v-if="v.msg">
                  <pre>{{v.msg}}</pre>
                </div>
                <div class="_meta">
                  {{v.datetime}}
                  <br />
                  {{v.email}}
                </div>
              </div>
            </div>

            <!-- 채팅입력부 -->
            <div id="_bottom">
              <v-form>
                <v-container grid-list-xl>
                  <v-layout wrap>
                    <v-flex xs12>
                      <v-text-field
                        v-model="msg"
                        outlined
                        label="Message"
                        type="text"
                        @keypress.enter.prevent="_chat"
                        @keypress.ctrl.enter.prevent="_new_line"
                      >
                        <template v-slot:append>
                          <v-fade-transition leave-absolute>
                            <i
                              class="fa fa-paper-plane"
                              @click="_chat"
                              aria-hidden="true"
                              style="color:blue"
                            ></i>
                            <!-- 전송버튼 -->
                          </v-fade-transition>
                        </template>
                      </v-text-field>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-form>
            </div>
             
          </template>
        </div>
      </v-flex>
     
    </v-layout>
  </v-container>
</template>

<script>
import firebase from "firebase/app";
import firebaseservice from './firebaseservice'
import "firebase/database";
import { mapActions } from "vuex";



const database = firebase.database();
var users_ref = database.ref("users");


function setScrollToBottom(id) {
  var target = document.getElementById(id);
  target.scrollTop = target.scrollHeight - target.offsetHeight;
}

export default {

  props: {
    Id: {}
  },

  data() {
    return {
      me: this.$store.state.data.user,
      loading: false,
      uid: "",
      email: "",
      pw: "",
      chat: {},
      users: {},
      msg: "",
      user_list_show: false,
      room_number : ''
      
    };
  },

  created() {
    if (
      localStorage.getItem("token") !== undefined &&
      localStorage.getItem("token") !== null
    ) {
      var result = this.chatUser(localStorage.getItem("token")).then(value => {
        console.log(value.email);
        this.email = value.email
        this.uid = value.name
        console.log(this.email)
        if (value == false) {
          console.log('로그인안돼있음')
        }
      }
      ) 
    } else {
    console.log('뭐여')
    }

    var z = this;
    console.log('몇 번째방?')
    console.log(this.Id)
    var chat_ref = database.ref(this.Id); 
    this.room_number = this.Id
    // 새로 들어온 메시지 입력하기
    chat_ref.on("child_added", d => {
      // 새로 추가된 행위
      this.$set(this.chat, d.key, d.val()); // this.chat 에  d.key 의 값으로 d.val 을 넣어라. 즉, chat = { {d.key:d.val()}} 상태
      this.$nextTick(() => {
        setScrollToBottom("_chat");
      });
    });
  },
  mounted(){
    console.log(this.Id)
  },

  methods: {
    ...mapActions("data", ["chatUser"]),
    _chat() {
      var newdate = new Date();
      var month = newdate.getMonth() + 1;
      var day = newdate.getDay();
      var hour = newdate.getHours();
      var min = newdate.getMinutes();
      var timestamp = month + "/" + day + " " + hour + ":" + min;

      if (!this.msg || event.ctrlKey) return;
      var chat_ref = database.ref(this.Id); 
      chat_ref.push().set({
        msg: this.msg,
        datetime: timestamp,
        uid: this.uid,
        email: this.email
      });
      this.msg = "";
    },
    _new_line() {
      this.msg += "\n";
    }
  }
};
</script>

<style>
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

body {
  margin: 500;
  padding: 0;
  background-color: gainsboro;
} /* #_root {  position: absolute;  top: 0;  left: 0;  width: 100%;  height: 100%;} */
._btn {
  display: inline-block;
  width: 150px;
  height: 40px;
  font-size: 17px;
  line-height: 40px;
  margin-top: 10px;
  background-color: #000;
  color: #fff;
  text-align: center;
  cursor: pointer;
  cursor: hand;
}
._btn._right {
  float: right;
}
._btn._wide {
  width: 310px !important;
}
._btn_2 {
  display: inline-block;
  width: auto;
  height: 20px;
  font-size: 17px;
  line-height: 20px;
  margin-top: 10px;
  color: #fff;
  text-align: center;
  cursor: pointer;
  cursor: hand;
}
._btn_2._right {
  float: right;
}
._btn_write {
  display: inline-block;
  float: right;
  width: 100px;
  height: 100px;
  font-size: 17px;
  line-height: 100px;
  background-color: white;
  color: #000;
  text-align: center;
  cursor: pointer; /* cursor: hand; */
} /* #_login_form {  position: absolute;  width: 310px;  height: 200px;  top: calc(50% - 100px);  left: calc(50% - 155px);}#_login_form input {  width: 310px;  height: 40px;  border: 1px solid #000;  font-size: 20px;  padding: 5px;  margin-top: 10px;} */
#_top {
  height: 60px;
  background-color: dimgrey;
  padding: 0px 15px;
}
#_chat {
  height: calc(100% - 200px);
  overflow-y: auto;
} /* #_file {  height: 40px;  background-color: dimgrey;  padding: 0px 15px;} */
#_bottom {
  width: 100%;
  height: 100px; /* background-color: #fff; */
}
#_bottom textarea {
  width: calc(100% - 100px);
  height: 100px;
  border: 0;
  vertical-align: middle;
  padding: 5px;
  font-size: 15px;
}
#_user_list {
  position: absolute;
  top: 60px;
  left: -1000px;
  width: 500px;
  max-width: 100%;
  height: calc(100% - 200px);
  background-color: #fff;
  z-index: 100;
  transition: all 0.5s ease-out;
  padding: 20px;
}
#_user_list._show {
  left: 0;
}
#_user_list > div {
  margin-top: 10px;
  font-size: 12px;
}
#_chat ._chat {
  clear: both;
} /* display:block; */ /* 왼쪽 텍스트 상자 */
#_chat ._chat > div {
  display: inline-block;
}
#_chat ._chat._right > div {
  float: right;
} /* 왼쪽 대화상자 */
#_chat ._chat ._msg,
#_chat ._chat ._file {
  float: left;
  font-weight: bold;
  max-width: 80%;
  padding: 5px 10px;
  margin: 10px;
  color: #fff;
  background-color: #00c6da;
  border-radius: 10px;
}
#_chat ._chat ._file img {
  display: block;
  max-width: 200px;
  margin-top: 10px;
} /* 오른쪽 대화상자 */
#_chat ._chat._right ._msg,
#_chat ._chat._right ._file {
  color: antiquewhite;
  font-weight: bold;
  float: right;
  background-color: #ee591f;
}
#_chat ._chat ._msg pre {
  word-break: break-all;
  white-space: pre-wrap;
}
#_chat ._chat ._meta {
  margin-top: 15px;
  font-size: 9px;
  color: #777;
}
#_chat ._chat._right ._meta {
  text-align: right;
}
#_file input {
  display: none;
}

/* 테스트 */
.messages {
  width: 200px;
  height: 200px;
  margin: 0 auto;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  font: 16px/1.3 sans-serif;
  overflow: auto;
  padding: 0;
  background: linear-gradient(rgb(255, 143, 178) 0%, rgb(167, 151, 255) 50%, rgb(0, 229, 255) 100%);
}

.messages:after {
  content: '';
  background: white;
  flex: 1;
  pointer-events: none;
}

.messages li {
  list-style-type: none;
  display: flex;
  flex-direction: row-reverse;
  overflow: hidden;
  border-style: solid;
  border-color: white;
  border-width: 2px 16px 2px 8px;
  flex: 0 0 auto;
}

.messages li.mine {
  flex-direction: row;
  border-right-width: 8px;
  border-left-width: 16px;
}

.messages li:first-child {
  border-top-width: 10px;
}

.messages li:last-child {
  border-bottom-width: 10px;
}

.messages li:before {
  content: '';
  flex: 1;
  background: white;
  pointer-events: none;
}

.messages li span {
  background: #eee;
  padding: 8px;
  position: relative;
}

.messages li span:before {
  content: '';
  position: absolute;
  left: -8px;
  top: -8px;
  bottom: -8px;
  right: -8px;
  border: 8px solid white;
  border-radius: 16px;
  pointer-events: none;
}

.messages li.mine span {
  background: none;
  color: white;
}
</style>