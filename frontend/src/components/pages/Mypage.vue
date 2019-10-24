<template>
<div class="hihi">
<div class="aboutme">
  <div class="left-content">
    <img src="../../DdakJeongE.png" alt="avatar">
  </div>
  <div class="right-content">
    <span class="greeting">Hello</span>
    <h2 class="my-name">
      {{user}}
    </h2>
    <div class="detail-infor">
    <div class="labels">
      <p>Name</p>
      <p>Email</p>
      <p>Tier</p>
      <p>Make with</p>
      <p>Created at</p>
    </div>
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
import router from "../../router"
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState({
      user : state => state.data.user,
    })
  }
};
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

<style>


.hihi{
  font-family: "Roboto", sans-serif;
  background-color: #e9e9e9;
  color: #222;
  display: flex;
  height: 100vh;
  justify-content: center;
  padding: 0;
  margin: 0;
  text-align : left;
}

.aboutme{
  display: flex;
  height : 500px;
  grid-template-columns : 2fr 3fr;
  align-items: center;
  grid-gap : 1rem;
  background-color : #f9f9f9;
  padding-top : 1rem;
  box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
  border-radius : 5px;
  position: relative;
  padding : 10px;
  margin : 50px;

}

.left-content{
    margin-left : 2rem;
    margin-right : 2rem;
}

.left-content img{
  width : 200px;
  background-size : cover;
}

.right-content{
  margin-top: 5px;
  margin-right: 10px;
}
.greeting{
  background-color : #FF73C8;
  display : inline-block;
  padding : .5rem 1rem;
  position : relative;
  font-size: 1.2rem;
  margin-bottom : .5rem;
  color : #f2f2f2;
}

.greeting:before{
  content: '';
  width:0;
  height:0;
  border: 6px solid;
  position: absolute;
  top: 100%;
  left:0;
  border-color: transparent;
  border-top-color: #FF73C8;
  border-left-color: #FF73C8;
}

.my-name{
    font-size : 1.5rem;
    font-weight: 400;
}

.my-name span{
  font-weight: 400;
}
p{
    margin : .6rem;
}
 
.detail-infor{
  display: grid;
  grid-template-columns : 1fr 2fr;
  align-items : center;
}

.labels{
  font-weight: 600;
  margin-right: 2rem;
}

.bottom-content{ 
    
  position: absolute;
  top: 95%;
  left: 50%;
  transform: translateX(-50%);
  background: #ffe4af;
  width: 100%;
  padding: 7px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}

.bottom-content a{
  color: black;
  text-decoration: none;
  opacity: 0.8;
  transition: 200ms;
  font-size: 24px;
  margin:0  10px;
}

.bottom-content a:hover{
opacity: 1;
}

.form-group{
  margin-bottom: 20px;
}
.form-wrap{
  padding : 10px;
}

.formcon{
  padding-left: 40px;
  padding-right : 40px;
}


.movebtn{
  background-color: transparent;
  display:inline-block;
  width:100%;
  background-image: none;
  padding: 8px 10px;
  border-radius: 0;
  -webkit-transition: all 0.5s;
  -moz-transition: all 0.5s;
  transition: all 0.5s;
  -webkit-transition-timing-function: cubic-bezier(0.5, 1.65, 0.37, 0.66);
  transition-timing-function: cubic-bezier(0.5, 1.65, 0.37, 0.66);
}


.buttons {
  padding: 8px 12px;
  margin: 4px 0;
  font-family: 'Montserrat', sans-serif;
  border: 2px solid #78788c;
  background: 0;
  color: #5a5a6e;
  cursor: pointer;
  transition: all .3s;
}

.movebtnsu {
  border: 2px solid #3e3b4e;
  color: #ffffff;
  background-color: #3e3b4e;
}
.buttons:hover {
  background: #646171;
  color: #fff;
  border-color: #646171;
  box-shadow: 0px 0 5px 0 #646171;
}
</style>