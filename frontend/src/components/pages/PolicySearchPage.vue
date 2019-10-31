<template>
    <div class="policy_search_main">
        <div class="policy_search_header">
            <div class="policy_search_head">분류별 검색</div>
            <div class="policy_search_head">전체 보기</div>
        </div>
        <div class="policy_search_content">
            <div class="policy_search_A">
                <div class="policy_search_A_header">생애주기</div>
                <div class="policy_search_A_content"><img   src="../../images/Pregnant_woman.png" style="width:100%;"><img   src="../../images/Infants.png" style="width:100%;"><img   src="../../images/Teenager.png" style="width:100%;"><img   src="../../images/Youth.png" style="width:100%;"><img   src="../../images/Middle_age.png" style="width:100%;"><img   src="../../images/Old_age.png" style="width:100%;"></div>
            </div>
            <div class="policy_search_B">
                <div class="policy_search_B_header">가구상황</div>
                <div class="policy_search_B_content"><img   src="../../images/Disabled.png" style="width:100%;"><img   src="../../images/Single_parent.png" style="width:100%;"><img   src="../../images/Multicultural.png" style="width:100%;"><img   src="../../images/Low_income.png" style="width:100%;"></div>
            </div>
            <div class="policy_search_C">
                <div class="policy_search_C_header">관심주제</div>
                <div class="policy_search_C_content"><img   src="../../images/Education.png" style="width:100%;"><img   src="../../images/Employ.png" style="width:100%;"><img   src="../../images/Dwelling.png" style="width:100%;"><img   src="../../images/Health.png" style="width:100%;"><img   src="../../images/Population_Finance.png" style="width:100%;"><img   src="../../images/Culture.png" style="width:100%;"></div>
            </div>
        </div>
    </div>    
</template>
<script>
export default {
    
}
</script>
<style>
.policy_search_main{
    width: 80vw;
    height: 50vh;
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
    align-items: center;
}

.policy_search_A_content img, .policy_search_C_content img{
    width: 33% !important;
}
.policy_search_B_content img{
    width: 45%  !important;
}
</style>