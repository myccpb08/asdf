<template>
<div class="hihi">
  <!-- <img class="imgTwo" src="../../wood.jpg" style="opacity: 0.64; position:absolute; width:100%; height:100%;"> -->
<div class="aboutme">
  <div class="left-content">
    <img src="../../images/D_logo.png" alt="avatar" style="width: 200px; height: 200px; overflow:hidden; border-radius: 100%;">
    <div class="labels">
      <p>Nickname : </p>
      <p>Email : </p>
      <p>Age : </p>
      <p>Gender : </p>
      <p>Area : </p>
    </div>
    <div class="detail-infor">
      <div class="infor">
            <!-- <p v-if="modifymode==false">{{this.$store.state.user.displayName}}</p>
                <v-text-field
                  v-else
                  v-model="usrName"
                  label="Name"
                  required
                  class="notranslate"
                  :rules="nameRules"
                ></v-text-field>
            <p>{{this.$store.state.user.email}}</p>
            <p>{{this.$store.state.user.tier}}</p>
            <p>{{this.$store.state.user.type}}</p>
            <p>{{this.$store.state.user.created_at.toString().slice(4,16)}}</p> -->
      </div>
    </div>
  </div>
  <div style="border-left: 1px solid gray; height: 100%; width: 1px;"></div>
  <div class="right-content">
    <div class="btn_div">
      <div class="mypage_button">
        <div class="btn_hover_line_up"></div>
        <span>rrrrrr</span>
        <div class="btn_hover_line_down"></div>
      </div>
      <button class="mypage_btn">내가 찾아본 정책</button>
      <div class="divider"></div>
      <button class="mypage_btn">내 정보</button>
      <div class="divider"></div>
      <button class="mypage_btn">내 정보 수정</button>
    </div>
    <div class="subabout">
      <div style="width:100%;">
        <div class="sub_contents_left">
        <h2 class="my-name">
          니이름
        </h2>
        </div>
        <div class="sub_contents_right">
          <h2>Right</h2>
        </div>
      </div>
      
    </div>
  <div>
    <!-- <span class="greeting">Hello</span> -->
    
  </div>
  </div>
<!---->
  <!-- <div class="bottom-content" > -->
    <!-- <v-dialog
      v-model="passchange"
      width="400"
      v-if="this.$store.state.user.type!='facebook'&&this.$store.state.user.type!='google'"
    > -->
    <!-- <template v-slot:activator="{on}"> -->
      <!-- <v-btn  v-on="on" color="#fcc6f7">
        비밀번호 변경</v-btn> -->
    <!-- </template> -->
    <!-- <v-card>
      <h2 class="lining regiheight">
        비밀번호 변경</h2>
        <div class="form-wrap" style="position: relative;">
          
          <div class="form-group">
          <div class="relative">
            <v-text-field
              v-model="pass"
              type="password"
              label="PassWord"
              :rules="passRules"
              required
              class="formcon notranslate"
              @keyup.enter="changePass"
            ></v-text-field>
          </div>
          </div>

          <div class="form-group">
          <div class="relative">
            <v-text-field
              v-model="passchk"
              type="password"
              label="PassWord Confirm"
              :rules="passcheckRules"
              required
              class="formcon notranslate"
              @keyup.enter="changePass"
            ></v-text-field>
          </div>
          </div>

          <button class="buttons movebtn movebtnsu " @click="changePass">
            Change PassWord
            <i class="fa fa-fw fa-lock"></i>
          </button >

        </div>
    </v-card> -->
    <!-- </v-dialog> -->
    
    <!-- <v-btn v-if="modifymode==false" v-on:click="modifymode=true" color="#fcc6f7">
      수정하기
    </v-btn>
    <v-btn v-else v-on:click="modify"  color="#fcc6f7">
      수정하기
    </v-btn> -->
    

    <!--admin@admin.com 은 탈퇴하지 못함 -->
    <!-- <v-btn>탈퇴하기</v-btn> -->
    <!-- <v-btn
      v-if="this.$store.state.user.email!='admin@admin.com'"
      @click.stop="withdraw=true" color="#fcc6f7">
        탈퇴하기</v-btn> -->
        <!-- <v-dialog v-model="withdraw" max-width="400">
          <v-card>
            <v-card-title> 탈퇴 하시겠습니까?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                text
                @click="Leaving(true)">
                예</v-btn>
              <v-btn
                text
                @click="Leaving(false)">
                아니오</v-btn>
              </v-btn>
            
            </v-card-actions>
          </v-card>
        </v-dialog> -->
  <!-- </div> -->
</div>
</div>

</template>
<script>
// import firebase from "firebase";
// import FirebaseService from '@/services/FirebaseService'
// export default {
//   data(){
//     return {
//         withdraw: false,
//         passchange : false,
//         usrName:"",
//         modifymode: false,
//         pass: "",
//         passchk :"",
//         passRules: [
//           v => !!v || "PassWord is required",
//           v => v.length > 7 || "Password is more than 8 characters"
//         ],

//         passcheckRules: [
//           v => !!v || "You have to check Password",
//           v => v === pass || "Isn't match with Password"
//         ],
//         nameRules: [v => !!v || "Name is required"]
//     }
//   },
//     methods: {
//       changePass(){ //비밀번호를 바꿈
//         if( !this.pass ){
//           alert("You have to enter your password");
//           return;
//         }
//         if( !this.passchk){
//           alert("You have to check password");
//           return;
//         }
//         if( this.pass!=this.passchk){
//           alert("Password is not verified");
//           return;
//         }
//         var currentuser = firebase.auth().currentUser;

//         currentuser.updatePassword(this.pass)
//         .then(()=>{
//           alert(this.$store.state.user.displayName+" 님의 비밀번호가 바뀌었습니다.");
//           this.passchange = false;
//         }).catch(function(err){
//           alert(err);
//         });
//       },
//       Leaving(agree){ //탈퇴함
//         if( agree == true){
          
//           this.withdraw = false;
          
//           var currentuser = firebase.auth().currentUser;
//           // db에서 삭제
//           FirebaseService.deleteUser(currentuser.uid);
//           //erase local storage 
//           this.$store.state.accessToken = "";
//           this.$store.state.user = "";
//           localStorage.setItem("accessToken", this.$store.state.accessToken);
//           localStorage.setItem("user", this.$store.state.user);
         
//           currentuser.delete().then(function(){
//             window.location.replace("/");
//           }).catch(function(err){
//             alert(err)
//           });
          
//         }else{
//           this.withdraw = false;
//         }

//       },
//       modify(){
//         if( !this.usrName){
//           alert("이름을 적으세요");
//         }
//         var currentuser = firebase.auth().currentUser;
//         const firestore = firebase.firestore();
//         firestore.collection("users").doc(currentuser.uid).update({
//           dispplayName : this.usrName
//         }).then(()=>{
//           modifymode = false;
//         });
//       }
//     },
//     computed: {
//       passVerification() {
//         return this.pass === this.passchk
//           ? true
//           : "Have to verify password";
//       }
//     }
// };

</script>