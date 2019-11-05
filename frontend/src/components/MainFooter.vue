<template>
    <footer>
        <div>
            <!-- <h3>딱정이<br>딱 맞는 정책은 이거다!</h3>
            <address>abcd@abc.com</address> -->
            <hr>
            <div class="OntheImage">
                <img class="imgTwo" src="../images/footerimg.png" style="width:40%;">
                <p style="padding-top:2%; padding-left:1.2%; font-size:13px; text-align:left; position:left; z-index: 1;">사회보장정보원(04554) 서울특별시 중구 퇴계로 173(충무로3가) bokjiro@ssis.or.kr
                <br>보건복지부(30113) 세종특별자치시 도움4로 13(어진동) 정부세종청사 10동 보건복지상담센터 129</p>
            </div>
        </div>
    </footer>
    
</template>

<script>

</script>
<style>
    .OntheImage {
        position: relative;
        text-align: center;
    }
    /* .Cent {
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    } */
    #MainFooter {
        /* 중앙정렬 */
        width: 100%;
        margin: 0 auto;
        margin-bottom: 10px;

        /* 테두리 */
        box-sizing: border-box;
        padding: 3%;
        background-color: whitesmoke;

        /* 글자정렬 */
        text-align: center;
    }
    .imgOne {
        margin-top: 1%;
        margin-left: 3%;
        float: left;
       
    }
    .imgTwo {
        float:right;
        position: relative;
        z-index: 0;
    }
</style>