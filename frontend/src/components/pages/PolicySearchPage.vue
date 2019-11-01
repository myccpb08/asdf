<template>
    <v-container>
        <div class="policy_search_main">
            <div class="policy_search_header">
                <div class="policy_search_head">분류별 검색</div>
                <div class="policy_search_head" style="cursor:pointer;" @click="goPage('00')">전체 보기</div>
            </div>
            <div class="policy_search_content">
                <div class="policy_search_A">
                    <div class="policy_search_A_header">생애주기</div>
                    <div class="policy_search_A_content">
                        <div @click="goPage('01')" class="a_div policy">
                            <img   src="../../images/Pregnant_woman.png" style="width:100%;">
                            <p>임신·출산</p>
                        </div>
                        
                        <div @click="goPage('02')" class="a_div policy">
                            <img   src="../../images/Infants.png" style="width:100%;">
                            <p>영유아</p>
                        </div>
                        
                        <div @click="goPage('03')" class="a_div policy">
                            <img   src="../../images/Teenager.png" style="width:100%;">
                            <p>아동·청소년</p>
                        </div>
                        <div @click="goPage('04')" class="a_div policy">
                            <img   src="../../images/Youth.png" style="width:100%;">
                            <p>청년</p>
                        </div>
                        <div @click="goPage('05')" class="a_div policy">
                            <img   src="../../images/Middle_age.png" style="width:100%;">
                            <p>중장년</p>
                        </div>
                        <div @click="goPage('06')" class="a_div policy">
                            <img   src="../../images/Old_age.png" style="width:100%;">
                            <p>노년</p>
                        </div>
                    </div>
                </div>
                <div class="policy_search_B">
                    <div class="policy_search_B_header">가구상황</div>
                    <div class="policy_search_B_content">
                        <div @click="goPage('07')" class="b_div policy">
                            <img   src="../../images/Disabled.png" style="width:100%;">
                            <p>장애인</p>
                        </div>
                        <div @click="goPage('08')" class="b_div policy">
                            <img   src="../../images/Single_parent.png" style="width:100%;">
                            <p>한부모</p>
                        </div>
                        <div @click="goPage('09')" class="b_div policy">
                            <img   src="../../images/Multicultural.png" style="width:100%;">
                            <p>다문화(새터민)</p>
                        </div>
                        <div @click="goPage('10')" class="b_div policy">
                            <img   src="../../images/Low_income.png" style="width:100%;">
                            <p>저소득층</p>
                        </div>
                    </div>
                </div>
                <div class="policy_search_C">
                    <div class="policy_search_C_header">관심주제</div>
                    <div class="policy_search_C_content">
                        <div @click="goPage('11')" class="c_div policy">
                            <img   src="../../images/Education.png" style="width:100%;">
                            <p>교육</p>
                        </div>
                        <div @click="goPage('12')" class="c_div policy">
                            <img   src="../../images/Employ.png" style="width:100%;">
                            <p>고용</p>
                        </div>
                        <div @click="goPage('13')" class="c_div policy">
                            <img   src="../../images/Dwelling.png" style="width:100%;">
                            <p>주거</p>
                        </div>
                        <div @click="goPage('14')" class="c_div policy">
                            <img   src="../../images/Health.png" style="width:100%;">
                            <p>건강</p>
                        </div>
                        <div @click="goPage('15')" class="c_div policy">
                            <img   src="../../images/Population_Finance.png" style="width:100%;">
                            <p>서민금융</p>
                        </div>
                        <div @click="goPage('16')" class="c_div policy">
                            <img   src="../../images/Culture.png" style="width:100%;">
                            <p>문화</p>
                        </div>
                        </div>
                </div>
            </div>
        </div>

        <div v-for="policy in ListSliced" :key=policy.id>
            <div class="policy_contents" @click="goService(policy.id)">
                <a style="text-decorations:none;color:black">
                    <h4>{{policy.title}}</h4><br>
                    {{policy.brief}}
                </a>
            </div>
        </div>

        <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
        
        
    </v-container>
</template>
<script>
import store from "../../store/modules/data.js";
import router from "../../router"
export default {
    data() {
        return {
            categoryId: "00",
            policies : [],
            listPerPage: 10,
            page: 1,
        };
    },

  async mounted() {
    this.getPolicys().then(result => {
      this.policies = result;
      console.log(this.policies)
    });
  },
  methods: {
    async getPolicys() {
        console.log(this.categoryId)
        return await this.$store.dispatch(
            "data/policySearch", this.categoryId
        );
    },

    goPage(n){
        
        var policy = document.querySelectorAll(".policy");
        var tempInt = parseInt(this.categoryId)-1;
        if(tempInt>=0){
            policy[tempInt].classList.remove("colorPink");
            policy[tempInt].classList.remove("colorYellow");
            policy[tempInt].classList.remove("colorBlue");
        }

        tempInt = parseInt(n)-1;
        if(tempInt <6 && tempInt >= 0){
            policy[tempInt].classList.add("colorPink");
        }else if(tempInt <9){
            policy[tempInt].classList.add("colorYellow");
        }else if(tempInt < 16){
            policy[tempInt].classList.add("colorBlue");
        }
        this.categoryId = n;
        this.getPolicys(n).then(response => {
                console.log(response)
                this.policies = response
            })
        // if(n <10){
        //     router.push("/policy/search/0"+n);
        // }else{
        //     router.push("/policy/search/"+n);
        // }
    },

    goService(n){
        router.push("/detailPolicy/"+n);
    }
  },

  computed: {
    // pagination related variables
    ListEmpty: function() {
      return this.policies.length === 0;
    },
    maxPages: function() {
      return Math.floor(
        (this.policies.length + this.listPerPage - 1) / this.listPerPage
      );
    },
    ListSliced: function() {
      return this.policies.slice(
        this.listPerPage * (this.page - 1),
        this.listPerPage * this.page
      );
    }
  }
};

</script>
<style>
.policy_search_main{
    width: 80vw;
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid black;
    border-radius: 7px;
}

.policy_search_header{
    width: 100%;
    height: 10%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid black;
    background-color: lightgray;
    border-radius: 7px;
}
.policy_search_head{
    width: 50%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.policy_search_head:nth-child(2){
    border-left: 1px solid black;
}

.policy_search_content{
    width: 100%;
    height: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.policy_search_A, .policy_search_B, .policy_search_C{
    width: 37.5%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-left: 1px solid black;
}

.policy_search_A{
    border-left: none;
}

.policy_search_B{
    width: 25%;
}

.policy_search_A_header, .policy_search_B_header, .policy_search_C_header{
    width: 100%;
    height: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid black;
}

.policy_search_A_content, .policy_search_B_content, .policy_search_C_content{
    width: 100%;
    height: 85%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    text-align: center;
    align-items: center;
}

.policy_search_A_content div, .policy_search_C_content div{
    width: 32% !important;
    height:48%;
    cursor:pointer;
    border-radius:7px;
}

.policy_search_A_content div:hover {
    background-color:#F16F85;
}
.policy_search_B_content div:hover {
    background-color:#FFB60F;
}
.policy_search_C_content div:hover {
    background-color:#57A5FF;
}

.colorPink{
    background-color:#F16F85;
}

.colorYellow{
    background-color:#FFB60F;
}

.colorBlue{
    background-color:#57A5FF;
}

.policy_search_B_content div{
    width: 49% !important;
    height:48%;
    cursor:pointer;
    border-radius:7px;
}

.policy_search_A_content img, .policy_search_B_content img, .policy_search_C_content img{
    width: 80% !important;
}

.policy_contents{
    width:80vw;
    margin-top: 5%;
    margin-bottom: 5%;
    padding: 4vh;
    border: 1px solid gray;
    border-radius: 7px;
}
</style>