<!-- 회원가입 페이지 --> 
<template>
    <v-container grid-list-md text-center>
        <v-layout justify-center wrap>
            <!-- 회원가입 폼-->
            <v-flex xs6>
                <div>회원가입!!</div>
                <SignUpForm :submit="signUp"/>
            </v-flex>
        </v-layout> 
    </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import SignUpForm from "../SignUpForm";
export default {
    components: {
        SignUpForm
    },
    data: () => ({}),
    methods: mapActions("data", ["signUp"])
};
</script>