<!-- 로그인 페이지 --> 
<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
            <!-- 로그인 폼-->
            <v-flex xs6>
                <div>로그인!!</div>
                <LoginForm :submit="checkLogin"/>
            </v-flex>
        </v-layout> 
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import LoginForm from "../LoginForm";
export default {
    components: {
        LoginForm
    },
    data: () => ({}),
    methods: mapActions("data", ["checkLogin"])
};
</script>