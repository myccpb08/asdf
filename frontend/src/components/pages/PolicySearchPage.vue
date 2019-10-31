<template>
    <v-container>
        <div class="policy_search_main">
            <div class="policy_search_header">
                <div class="policy_search_head">분류별 검색</div>
                <div class="policy_search_head" style="cursor:pointer;" @click="goPage(0)">전체 보기</div>
            </div>
            <div class="policy_search_content">
                <div class="policy_search_A">
                    <div class="policy_search_A_header">생애주기</div>
                    <div class="policy_search_A_content">
                        <div @click="goPage(1)">
                            <img   src="../../images/Pregnant_woman.png" style="width:100%;">
                            aaa
                        </div>
                        
                        <div @click="goPage(2)">
                            <img   src="../../images/Infants.png" style="width:100%;">
                        </div>
                        
                        <div @click="goPage(3)">
                            <img   src="../../images/Teenager.png" style="width:100%;">
                        </div>
                        <div @click="goPage(4)">
                            <img   src="../../images/Youth.png" style="width:100%;">
                            aaa
                        </div>
                        <div @click="goPage(5)">
                            <img   src="../../images/Middle_age.png" style="width:100%;">
                        </div>
                        <div @click="goPage(6)">
                            <img   src="../../images/Old_age.png" style="width:100%;">
                        </div>
                    </div>
                </div>
                <div class="policy_search_B">
                    <div class="policy_search_B_header">가구상황</div>
                    <div class="policy_search_B_content">
                        <div @click="goPage(7)">
                            <img   src="../../images/Disabled.png" style="width:100%;">
                        </div>
                        <div @click="goPage(8)">
                            <img   src="../../images/Single_parent.png" style="width:100%;">
                        </div>
                        <div @click="goPage(9)">
                            <img   src="../../images/Multicultural.png" style="width:100%;">
                        </div>
                        <div @click="goPage(10)">
                            <img   src="../../images/Low_income.png" style="width:100%;">
                        </div>
                    </div>
                </div>
                <div class="policy_search_C">
                    <div class="policy_search_C_header">관심주제</div>
                    <div class="policy_search_C_content">
                        <div @click="goPage(11)">
                            <img   src="../../images/Education.png" style="width:100%;">
                        </div>
                        <div @click="goPage(12)">
                            <img   src="../../images/Employ.png" style="width:100%;">
                        </div>
                        <div @click="goPage(13)">
                            <img   src="../../images/Dwelling.png" style="width:100%;">
                        </div>
                        <div @click="goPage(14)">
                            <img   src="../../images/Health.png" style="width:100%;">
                        </div>
                        <div @click="goPage(15)">
                            <img   src="../../images/Population_Finance.png" style="width:100%;">
                        </div>
                        <div @click="goPage(16)">
                            <img   src="../../images/Culture.png" style="width:100%;">
                        </div>
                        </div>
                </div>
            </div>
        </div>

        <div v-for="policy in ListSliced">
            <div class="policy_contents" @click="goService(policy.id)">
                <h4>{{policy.title}}</h4><br>
                <a>{{policy.brief}}</a>
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
            categoryId: this.$route.params.categoryId,
            policies : [],
            listPerPage: 10,
            page: 1
        };
    },

  async mounted() {
    this.getPolicys(this.categoryId).then(result => {
      this.policies = result;
      console.log(this.policies)
    });
  },
  methods: {
    async getPolicys(categoryId) {
        return this.$store.dispatch(
            "data/policySearch", categoryId
        );
    },

    goPage(n){
        if(n <10){
            router.push("/policy/search/0"+n);
        }else{
            router.push("/policy/search/"+n);
        }
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
    width: 33% !important;
    cursor:pointer;
}

.policy_search_B_content div{
    width: 45% !important;
    cursor:pointer;
}
.policy_search_A_content img, .policy_search_C_content img{
    width: 90% !important;
}
.policy_search_B_content img{
    width: 100%  !important;
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