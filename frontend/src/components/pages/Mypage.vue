<template>
<div class="hihi">
  <div class="aboutme">
    <div class="left-content">
      <div style="align-items: top;">
        <img src="../../images/D_logo.png" alt="avatar" style="width: 200px; height: 200px; overflow:hidden; border-radius: 100%;">
        <span class="greeting">Hello</span>
      </div>
      <div class="detail-infor">
        <div class="labels">
          <p>Nickname : </p>
          <p>Email : </p>
          <p>is_staff : </p>
          <p>Favorite : </p>
        </div>
        <div class="infor">
              <p>{{this.$store.state.data.user.name}}</p>
              <p>{{this.$store.state.data.user.username}}</p>
              <p>{{this.$store.state.data.user.is_staff}}</p>
              <p v-for="favorite in this.$store.state.data.user.favorite">
                <span>{{favorite}} </span>
              </p>
        </div>
      </div>
    </div>
    <div style="border-left: 1px solid gray; height: 100%; width: 1px;"></div>
    <div class="right-content">
      <div class="btn_div">
        <div class="mypage_button" @click="SearchList">
          <div class="btn_hover_line_up"></div>
          <button class="mypage_btn">내가 찾아본 정책</button>
          <div class="btn_hover_line_down"></div>
        </div>
        <div class="divider"></div>
        <div class="mypage_button" @click="EditInfo">
          <div class="btn_hover_line_up"></div>
          <button class="mypage_btn">내 정보 수정</button>
          <div class="btn_hover_line_down"></div>
        </div>
      </div>
      <div class="subabout">
        <EditUserInfoForm :submit="editUser" v-if="toglePage"/>
        <SearchListForm v-if="!toglePage"/>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import EditUserInfoForm from "../EditUserInfoForm";
import SearchListForm from "../SearchListForm";
import { mapState, mapActions } from "vuex";

export default {
  components: {
    EditUserInfoForm,
    SearchListForm
  },
  data: () => ({
    toglePage: false,
  }),
  mounted() {
    
  },
  methods: {
    SearchList() {
      this.toglePage = false
    },
    EditInfo() {
      this.toglePage = true
    },
    ...mapActions("data", ["editUser"])
  }
}

</script>

<style>
.hihi{
  font-family: "Roboto", sans-serif;
  background-color: #e9e9e9;
  color: #222;
  width:100%;
  display: flex;
  height: 80vh;
  justify-content: center;
  align-items: center;
  padding: 0;
  margin: 0;
  text-align : left;
}

.aboutme{
  width: 70%;
  display: flex;
  height : 500px;
  /* grid-template-columns : 2fr 3fr; */
  align-items: center;
  /* grid-gap : 1rem; */
  background-color : #f9f9f9;
  box-shadow: 0px 16px 32px rgba(0,0,0,0.3);
  border-radius : 5px;
}
.subabout{
  width: 100%;
  height: 88%;
  padding-top: 50px;
  text-align: -webkit-center;
    /* padding : 10px; */
    /* background-color:rgb(212, 212, 212); */
    /* border-radius : 5px; */
    /* box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.5) inset; */
}

.left-content{
    /* margin-left : 2rem; */
    padding-left: 3%;
    width: 40%;
    height: 450px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    position: relative;
}



.left-content img{
  width : 100%;
  background-size : cover;
}

.right-content{
  width: 60%;
  height: 100%;
  display: flex;
  flex-direction: column;
  /* margin-top: 5px;
  margin-right: 10px;
  padding-left: 10%;
  padding-right: 10%; */
}
.sub_contents_left{
  display: inline-flex;
  width: 50%;
  padding: 1%;
}
.sub_contents_right{
  display: inline-flex;
  width: 50%;
  padding: 1%;
}
.btn_div{
  width: 100%;
  height: 12%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0px 1px 0px 0px rgba(0,0,0,0.2);
}

.divider{
  width: 1px;
  height: 80%;
  background-color: rgba(0,0,0,0.2);
}

.mypage_button{
  width: 49%;
  height: 100%;
  background-color:F9F9F9;
  color:F9F9F9;
  border:none;
  font-size:1em;
  cursor:pointer;
  transition: all 0.8s;
  display: flex;
  flex-direction: column;
  position: relative;
  align-items: center;
  justify-content: center;
  -webkit-text-fill-color: orange;
}
.btn_hover_line_up{
  background-color: orange;
  position: absolute;
  top: 0;
  right: 0;
  width: 0;
  height: 3px;
  
}

.btn_hover_line_down{
  background-color: orange;
  position: absolute;
  left: 0;
  bottom: 0;
  width: 0;
  height: 3px;
}

.mypage_button:hover .btn_hover_line_up,
.mypage_button:hover .btn_hover_line_down{
  width: 100%;
  transition: width 0.8s;
}

.mypage_button:hover{
  background-color: F9F9F9;
  color:#fff;
}
/* .mypage_btn{
  width: 33.3%;
  height: 100%;
  background:#1AAB8A;
  color:#fff;
  border:none;
  position:relative;
  font-size:1em;
  padding:0 2em;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
}
.mypage_btn:hover{
  background:#fff;
  color:#1AAB8A;
}
.mypage_btn:before,.mypage_btn:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #1AAB8A;
  transition:400ms ease all;
}
.mypage_btn:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
.mypage_btn:hover:before,.mypage_btn:hover:after{
  width:100%;
  transition:800ms ease all;
} */

.greeting{
  background-color : orange;
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
  border-top-color: orange;
  border-left-color: orange;
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
  align-content : center;
  color: gray;
}

.labels{
  font-weight: 600;
  margin-right: 0.5rem;
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

<style scoped>

</style>